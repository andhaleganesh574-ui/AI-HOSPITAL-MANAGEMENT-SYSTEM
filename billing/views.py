from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404

from .models import Bill
from patients.models import Patient


def billing(request):

    data = Bill.objects.select_related(
        'patient'
    ).all().order_by('-bill_date')

    patients = Patient.objects.all().order_by('name')

    return render(
        request,
        'billing/billing.html',
        {
            'data': data,
            'patients': patients
        }
    )


def bill_save(request):

    if request.method == 'POST':

        patient = get_object_or_404(
            Patient,
            id=request.POST.get('patient')
        )

        consultation = Decimal(
            request.POST.get('consultation_fee') or 0
        )

        medicine = Decimal(
            request.POST.get('medicine_charges') or 0
        )

        laboratory = Decimal(
            request.POST.get('laboratory_charges') or 0
        )

        room = Decimal(
            request.POST.get('room_charges') or 0
        )

        other = Decimal(
            request.POST.get('other_charges') or 0
        )

        discount = Decimal(
            request.POST.get('discount') or 0
        )

        tax = Decimal(
            request.POST.get('tax') or 0
        )

        paid = Decimal(
            request.POST.get('paid_amount') or 0
        )

        total = (
            consultation +
            medicine +
            laboratory +
            room +
            other +
            tax -
            discount
        )

        if paid >= total:
            status = 'Paid'
        elif paid > 0:
            status = 'Partial'
        else:
            status = 'Pending'

        Bill.objects.create(
            patient=patient,
            invoice_number=request.POST.get(
                'invoice_number'
            ),
            consultation_fee=consultation,
            medicine_charges=medicine,
            laboratory_charges=laboratory,
            room_charges=room,
            other_charges=other,
            discount=discount,
            tax=tax,
            total_amount=total,
            paid_amount=paid,
            payment_method=request.POST.get(
                'payment_method'
            ),
            payment_status=status,
            notes=request.POST.get('notes')
        )

        return redirect('billing')

    return redirect('billing')


def bill_edit(request, id):

    bill = get_object_or_404(
        Bill,
        id=id
    )

    patients = Patient.objects.all().order_by('name')

    return render(
        request,
        'billing/bill_edit.html',
        {
            'bill': bill,
            'patients': patients
        }
    )


def bill_update(request, id):

    bill = get_object_or_404(
        Bill,
        id=id
    )

    if request.method == 'POST':

        bill.patient = get_object_or_404(
            Patient,
            id=request.POST.get('patient')
        )

        bill.invoice_number = request.POST.get(
            'invoice_number'
        )

        bill.consultation_fee = Decimal(
            request.POST.get('consultation_fee') or 0
        )

        bill.medicine_charges = Decimal(
            request.POST.get('medicine_charges') or 0
        )

        bill.laboratory_charges = Decimal(
            request.POST.get('laboratory_charges') or 0
        )

        bill.room_charges = Decimal(
            request.POST.get('room_charges') or 0
        )

        bill.other_charges = Decimal(
            request.POST.get('other_charges') or 0
        )

        bill.discount = Decimal(
            request.POST.get('discount') or 0
        )

        bill.tax = Decimal(
            request.POST.get('tax') or 0
        )

        bill.paid_amount = Decimal(
            request.POST.get('paid_amount') or 0
        )

        bill.total_amount = (
            bill.consultation_fee +
            bill.medicine_charges +
            bill.laboratory_charges +
            bill.room_charges +
            bill.other_charges +
            bill.tax -
            bill.discount
        )

        if bill.paid_amount >= bill.total_amount:
            bill.payment_status = 'Paid'
        elif bill.paid_amount > 0:
            bill.payment_status = 'Partial'
        else:
            bill.payment_status = 'Pending'

        bill.payment_method = request.POST.get(
            'payment_method'
        )

        bill.notes = request.POST.get('notes')

        bill.save()

        return redirect('billing')

    return redirect(
        'bill_edit',
        id=id
    )


def bill_delete(request, id):

    bill = get_object_or_404(
        Bill,
        id=id
    )

    bill.delete()

    return redirect('billing')
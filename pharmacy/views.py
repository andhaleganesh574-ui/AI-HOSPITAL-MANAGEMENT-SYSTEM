from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine


def pharmacy(request):

    data = Medicine.objects.all().order_by('name')

    return render(
        request,
        'pharmacy/pharmacy.html',
        {'data': data}
    )


def medicine_save(request):

    if request.method == 'POST':

        Medicine.objects.create(
            name=request.POST.get('name'),
            generic_name=request.POST.get('generic_name'),
            category=request.POST.get('category'),
            manufacturer=request.POST.get('manufacturer'),
            batch_number=request.POST.get('batch_number'),
            expiry_date=request.POST.get('expiry_date'),
            quantity=request.POST.get('quantity'),
            reorder_level=request.POST.get('reorder_level'),
            purchase_price=request.POST.get('purchase_price'),
            selling_price=request.POST.get('selling_price'),
            supplier=request.POST.get('supplier'),
            description=request.POST.get('description')
        )

        return redirect('pharmacy')

    return redirect('pharmacy')


def medicine_edit(request, id):

    medicine = get_object_or_404(
        Medicine,
        id=id
    )

    return render(
        request,
        'pharmacy/medicine_edit.html',
        {'medicine': medicine}
    )


def medicine_update(request, id):

    medicine = get_object_or_404(
        Medicine,
        id=id
    )

    if request.method == 'POST':

        medicine.name = request.POST.get('name')
        medicine.generic_name = request.POST.get('generic_name')
        medicine.category = request.POST.get('category')
        medicine.manufacturer = request.POST.get('manufacturer')
        medicine.batch_number = request.POST.get('batch_number')
        medicine.expiry_date = request.POST.get('expiry_date')
        medicine.quantity = request.POST.get('quantity')
        medicine.reorder_level = request.POST.get('reorder_level')
        medicine.purchase_price = request.POST.get('purchase_price')
        medicine.selling_price = request.POST.get('selling_price')
        medicine.supplier = request.POST.get('supplier')
        medicine.description = request.POST.get('description')

        medicine.save()

        return redirect('pharmacy')

    return redirect(
        'medicine_edit',
        id=id
    )


def medicine_delete(request, id):

    medicine = get_object_or_404(
        Medicine,
        id=id
    )

    medicine.delete()

    return redirect('pharmacy')

def stock_in(request, id):

    medicine = get_object_or_404(
        Medicine,
        id=id
    )

    if request.method == 'POST':

        amount = int(request.POST.get('amount'))

        medicine.quantity += amount
        medicine.stock_in += amount

        medicine.save()

    return redirect('pharmacy')


def stock_out(request, id):

    medicine = get_object_or_404(
        Medicine,
        id=id
    )

    if request.method == 'POST':

        amount = int(request.POST.get('amount'))

        if amount <= medicine.quantity:

            medicine.quantity -= amount
            medicine.stock_out += amount

            medicine.save()

    return redirect('pharmacy')
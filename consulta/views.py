from django.shortcuts import render
from cadastro.models import Usuario
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime

import csv, xlwt

def consulta_home(request):
    return render(request, 'consulta.html')

def consulta_csv(request):
    usuarios = Usuario.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=consulta_usuarios' + str(datetime.now()) + '.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'usuario', 'nasc', 'senha'])
    campos_usuarios = usuarios.values_list('id', 'usuario', 'nasc', 'senha')
    for usuario in campos_usuarios:
        writer.writerow(usuario)
    return response

def consulta_json(request):
    usuarios = serializers.serialize('json', Usuario.objects.all())
    response = HttpResponse(usuarios, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=consulta_usuarios' + str(datetime.now()) + '.json'
    return response

def consulta_xlsx(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=consulta_usuarios' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Usuários')
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID', 'USUÁRIO', 'NASCIMENTO', 'SENHA']

    for col in range(len(columns)):
        ws.write(row_num, col, columns[col], font_style)
    
    font_style.font.bold = False

    rows = Usuario.objects.all().values_list('id', 'usuario', 'nasc', 'senha')

    for row in rows:
        row_num += 1
        for col in range(len(row)):
            ws.write(row_num, col, str(row[col]), font_style)
    
    wb.save(response)

    return response

with open("D:\\OneDrive\\Jugando con Python\\comarb\\do_my_work\\out.txt", "r") as f:
    text = f.read()
    #transacciones = []
    transacciones = [text[i:i+152]for i in range(0,len(text), 152)]
    # for i in range(0, len(text), 152):
    #     transacciones.append(text[i:i+152])
    #print(transacciones)

    trans_dic = {}
    for tran in transacciones:
        trans_dic["transaccion"] = tran[:7]
        trans_dic["cuit"] = tran[8:21]
        trans_dic["razon_social"] = tran[22:56].strip()
        trans_dic["tramite"] = tran[56:107].strip()
        trans_dic["estado"] = tran[107:137].strip()
        trans_dic["fecha_estado"] = tran[137:].strip()

print(trans_dic)
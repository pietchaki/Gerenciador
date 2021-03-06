#!/usr/bin/env python
# -*- coding: cp1252 -*-

import controller
import view
import viewCadastros
import model
from Tkinter import *
import tkFont as tkFont
import ttk as ttk

def mostra_dados_forn(event, tabela,pai):   
    id_item = tabela.identify('row',event.x,event.y)
    item = tabela.item(id_item)
    valores =  item.values()[2]

    popup = Toplevel()
    popup.title("Gerenciador - Dados Fornecedores")

    viewCadastros.tela_cad_forn(popup)

    filho = popup.winfo_children()
    filhos = filho[0].winfo_children()
    filhos[1].insert(0, valores[1])
    valor = str(valores[2])
    for index in range(len(valor)):                                 #necessario por causa da validacao do campo 'duracao campanha'
        filhos[3].insert(index, valor[index])
    filhos[4].configure(text="Alterar")
    filhos[4].configure(command=lambda: controller.alterar("lista_forn", popup, pai, {"classe":model.fornecedor,"id":valores[0],"nome_forn":filhos[1].get(), "dur_camp":filhos[3].get()}))

    botao_excluir = Button(filho[0], text="Excluir", command=lambda: controller.excluir("lista_forn",popup, pai,{"classe":model.fornecedor,"id":valores[0],"nome_forn":'', "dur_camp":''}))
    botao_excluir.grid(row=2,column=0, sticky=E, pady=10)


def mostra_dados_clie(event, tabela,pai):
    id_item = tabela.identify('row',event.x,event.y)
    item = tabela.item(id_item)
    valores =  item.values()[2]

    popup = Toplevel()
    popup.title("Gerenciador - Dados Clientes")

    viewCadastros.tela_cad_clie(popup)

    filho = popup.winfo_children()
    filhos = filho[0].winfo_children()
    filhos[1].insert(0, valores[1])     #nome                           #TODO melhorar => fazer função
    filhos[3].insert(0, valores[2])     #cpf
    filhos[5].insert(0, valores[6])     #tel res                        #carrega os valores da consulta do banco
    filhos[7].insert(0, valores[5])     #tel cel
    filhos[9].insert(0, valores[7])     #tel com
    filhos[11].insert(0, valores[3])     #email
    filhos[13].insert(0, valores[4])    #endereco

    filhos[14].configure(text="Alterar")
    filhos[14].configure(command=lambda: controller.alterar("lista_clie",popup, pai, {"classe":model.pessoa,"id":valores[0], "nome_pessoa":filhos[1].get(),
                                                                "email":filhos[9].get(),"endereco":filhos[11].get(),"tel_cel":filhos[5].get(),
                                                                 "tel_res":filhos[3].get(),"tel_com":filhos[7].get(),"tipo":0}))

    botao_excluir = Button(filho[0], text="Excluir", command=lambda: controller.excluir("lista_clie",popup, pai,{"classe":model.pessoa,"id":valores[0],"nome_pessoa": '',
                                                                "email": '',"endereco": '',"tel_cel": '', "tel_res": '',"tel_com": '',"tipo": 0}))
    botao_excluir.grid(row=8,column=1, sticky=W, pady=10)


def mostra_dados_vend(event, tabela, pai):
    id_item = tabela.identify('row',event.x,event.y)
    item = tabela.item(id_item)
    valores =  item.values()[2]

    popup = Toplevel()
    popup.title("Gerenciador - Dados Vendedores")

    viewCadastros.tela_cad_vend(popup)

    filho = popup.winfo_children()
    filhos = filho[0].winfo_children()
    filhos[1].insert(0, valores[1])     #nome                           #TODO melhorar => fazer função
    filhos[3].insert(0, valores[2])     #cpf
    filhos[5].insert(0, valores[6])     #tel res                        #carrega os valores da consulta do banco
    filhos[7].insert(0, valores[5])     #tel cel
    filhos[9].insert(0, valores[7])     #tel com
    filhos[11].insert(0, valores[3])     #email
    filhos[13].insert(0, valores[4])    #endereco

    comissoes = []
    filhos[15].configure(command= lambda: viewCadastros.inclui_comissao(comissoes,valores[0]))

    filhos[16].configure(text="Alterar")
    filhos[16].configure(command=lambda: controller.alterar("lista_vend", popup, pai, {"classe":model.vendedor, "id":valores[0], "nome_pessoa":filhos[1].get(), "email":filhos[9].get(),"endereco":filhos[11].get(), "tel_cel":filhos[5].get(), "tel_res":filhos[3].get(),"tel_com":filhos[7].get(),"tipo":1,"comissoes":comissoes }))

    botao_excluir = Button(filho[0], text="Excluir", command=lambda: controller.excluir(filho[0],popup, pai,{"classe":model.vendedor, "id":valores[0],"nome_pessoa": '', "email": '',"endereco": '',"tel_cel": '', "tel_res": '',"tel_com": '',"tipo": 1}))
    botao_excluir.grid(row=8,column=1, sticky=W, pady=10)


def mostra_dados_prod(event, tabela,pai):   
    id_item = tabela.identify('row',event.x,event.y)
    item = tabela.item(id_item)
    valores =  item.values()[2]

    popup = Toplevel()
    popup.title("Gerenciador - Dados Produto")

    var_forn = viewCadastros.tela_cad_prod(popup)

    filho = popup.winfo_children()
    filhos = filho[0].winfo_children()
    temp = str(valores[1])
    for index in range(len(temp)):                       #necessario  por causa da validacao do campo 
        filhos[1].insert(index, temp[index])            #codigo
    var_forn.set(valores[2])                                #fornecedor
    temp = str(valores[3])
    for index in range(len(temp)):                       #necessario  por causa da validacao do campo 
        filhos[5].insert(index, temp[index]) # quantidade
    filhos[7].insert(0, valores[4]) # descricao
    filhos[9].insert(0, valores[5]) # pcompra
    filhos[11].insert(0, valores[6]) # pvenda

    filhos[12].configure(text="Alterar")
    filhos[12].configure(command=lambda: controller.alterar("lista_prod", popup, pai, {"classe":model.produto,
                        "id":valores[0], "codigo": filhos[1].get(),"fornecedor": var_forn.get(),"qnt": filhos[5].get(),"desc": filhos[7].get(),
                                                                 "pcompra": filhos[9].get(),"pvenda": filhos[11].get()}))

    botao_excluir = Button(filho[0], text="Excluir", command=lambda: controller.excluir("lista_prod",popup, pai,{"classe":model.produto,
                    "id":valores[0],"codigo": "","fornecedor": "","qnt": "","desc": "", "pcompra": "","pvenda": ""}))
    botao_excluir.grid(row=7,column=0, sticky=E, pady=10)


def tela_lista_forn(root,cabecalhos, dados):
    view.limpa_tela(root)

    frame_lista_forn = LabelFrame(root, text="Listagem Fornecedores", padx=5, pady=5)
    frame_lista_forn.grid(padx=10, pady=10)    

    tabela = ttk.Treeview(columns=cabecalhos, show="headings")
    scroll_v = ttk.Scrollbar(orient="vertical", command=tabela.yview)
    scroll_h = ttk.Scrollbar(orient="horizontal", command=tabela.xview)
    tabela.configure(yscrollcommand=scroll_v.set, xscrollcommand=scroll_h.set)
    tabela.grid(column=0, row=0, sticky='nsew', in_=frame_lista_forn)
    scroll_v.grid(column=1, row=0, sticky='ns', in_=frame_lista_forn)
    scroll_h.grid(column=0, row=1, sticky='ew', in_=frame_lista_forn)
    frame_lista_forn.grid_columnconfigure(0, weight=1)
    frame_lista_forn.grid_rowconfigure(0, weight=1)

    for col in cabecalhos:
        tabela.heading(col, text=col.title(),command=lambda c=col: view.sortby(tabela, c, 0))
            # adjust the column's width to the header string
        tabela.column(col,width=tkFont.Font().measure(col.title()))
    for item in dados:
        tabela.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(val)
            if tabela.column(cabecalhos[ix],width=None) < col_w :
                tabela.column(cabecalhos[ix], width=col_w)

    tabela.bind("<Double-Button-1>", lambda event: mostra_dados_forn(event,tabela,root))

    #TODO colocar historico de vendas

def tela_lista_clie(root,cabecalhos, dados):
    view.limpa_tela(root)

    frame_lista_clie = LabelFrame(root, text="Listagem Clientes", padx=5, pady=5)
    frame_lista_clie.grid(padx=10, pady=10)    

    tabela = ttk.Treeview(columns=cabecalhos, show="headings")
    scroll_v = ttk.Scrollbar(orient="vertical", command=tabela.yview)
    scroll_h = ttk.Scrollbar(orient="horizontal", command=tabela.xview)
    tabela.configure(yscrollcommand=scroll_v.set, xscrollcommand=scroll_h.set)
    tabela.grid(column=0, row=0, sticky='nsew', in_=frame_lista_clie)
    scroll_v.grid(column=1, row=0, sticky='ns', in_=frame_lista_clie)
    scroll_h.grid(column=0, row=1, sticky='ew', in_=frame_lista_clie)
    frame_lista_clie.grid_columnconfigure(0, weight=1)
    frame_lista_clie.grid_rowconfigure(0, weight=1)

    for col in cabecalhos:
        tabela.heading(col, text=col.title(),command=lambda c=col: view.sortby(tabela, c, 0))
            # adjust the column's width to the header string
        tabela.column(col,width=tkFont.Font().measure(col.title()))
    for item in dados:
        tabela.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(val)
            if tabela.column(cabecalhos[ix],width=None) < col_w :
                tabela.column(cabecalhos[ix], width=col_w)

    tabela.bind("<Double-Button-1>", lambda event: mostra_dados_clie(event,tabela,root))

    #TODO colocar historico de vendas

def tela_lista_vend(root,cabecalhos, dados):
    view.limpa_tela(root)

    frame_lista_vend = LabelFrame(root, text="Listagem Vendedores", padx=5, pady=5)
    frame_lista_vend.grid(padx=10, pady=10)    

    tabela = ttk.Treeview(columns=cabecalhos, show="headings")
    scroll_v = ttk.Scrollbar(orient="vertical", command=tabela.yview)
    scroll_h = ttk.Scrollbar(orient="horizontal", command=tabela.xview)
    tabela.configure(yscrollcommand=scroll_v.set, xscrollcommand=scroll_h.set)
    tabela.grid(column=0, row=0, sticky='nsew', in_=frame_lista_vend)
    scroll_v.grid(column=1, row=0, sticky='ns', in_=frame_lista_vend)
    scroll_h.grid(column=0, row=1, sticky='ew', in_=frame_lista_vend)
    frame_lista_vend.grid_columnconfigure(0, weight=1)
    frame_lista_vend.grid_rowconfigure(0, weight=1)
    
    for col in cabecalhos:
        tabela.heading(col, text=col.title(),command=lambda c=col: view.sortby(tabela, c, 0))
            # adjust the column's width to the header string
        tabela.column(col,width=tkFont.Font().measure(col.title()))
    for item in dados:
        tabela.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(val)
            if tabela.column(cabecalhos[ix],width=None) < col_w :
                tabela.column(cabecalhos[ix], width=col_w)

    tabela.bind("<Double-Button-1>", lambda event: mostra_dados_vend(event,tabela,root))
    

def tela_lista_prod(root,cabecalhos, dados):
    view.limpa_tela(root)

    frame_lista_vend = LabelFrame(root, text="Listagem Produtos", padx=5, pady=5)
    frame_lista_vend.grid(padx=10, pady=10)    

    tabela = ttk.Treeview(columns=cabecalhos, show="headings")
    scroll_v = ttk.Scrollbar(orient="vertical", command=tabela.yview)
    scroll_h = ttk.Scrollbar(orient="horizontal", command=tabela.xview)
    tabela.configure(yscrollcommand=scroll_v.set, xscrollcommand=scroll_h.set)
    tabela.grid(column=0, row=0, sticky='nsew', in_=frame_lista_vend)
    scroll_v.grid(column=1, row=0, sticky='ns', in_=frame_lista_vend)
    scroll_h.grid(column=0, row=1, sticky='ew', in_=frame_lista_vend)
    frame_lista_vend.grid_columnconfigure(0, weight=1)
    frame_lista_vend.grid_rowconfigure(0, weight=1)
    
    for col in cabecalhos:
        tabela.heading(col, text=col.title(),command=lambda c=col: view.sortby(tabela, c, 0))
            # adjust the column's width to the header string
        tabela.column(col,width=tkFont.Font().measure(col.title()))
    for item in dados:
        tabela.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(val)
            if tabela.column(cabecalhos[ix],width=None) < col_w :
                tabela.column(cabecalhos[ix], width=col_w)

    tabela.bind("<Double-Button-1>", lambda event: mostra_dados_prod(event,tabela,root))

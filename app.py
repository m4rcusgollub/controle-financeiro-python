from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO_DADOS = "dados.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_dados(movimentacoes):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(movimentacoes, arquivo, indent=4, ensure_ascii=False)


def formatar_dinheiro(valor):
    return f"R$ {valor:.2f}"


def calcular_resumo(movimentacoes):
    total_receitas = 0
    total_gastos = 0

    for item in movimentacoes:
        if item["tipo"] == "receita":
            total_receitas += item["valor"]
        elif item["tipo"] == "gasto":
            total_gastos += item["valor"]

    saldo = total_receitas - total_gastos

    return total_receitas, total_gastos, saldo


@app.route("/")
def index():
    movimentacoes = carregar_dados()
    total_receitas, total_gastos, saldo = calcular_resumo(movimentacoes)

    return render_template(
        "index.html",
        movimentacoes=movimentacoes,
        total_receitas=total_receitas,
        total_gastos=total_gastos,
        saldo=saldo,
        formatar_dinheiro=formatar_dinheiro
    )


@app.route("/adicionar", methods=["POST"])
def adicionar_movimentacao():
    descricao = request.form.get("descricao")
    categoria = request.form.get("categoria")
    tipo = request.form.get("tipo")
    valor = request.form.get("valor")

    if not descricao or not categoria or not tipo or not valor:
        return redirect(url_for("index"))

    try:
        valor = float(valor.replace(",", "."))
    except ValueError:
        return redirect(url_for("index"))

    if valor <= 0:
        return redirect(url_for("index"))

    movimentacao = {
        "tipo": tipo,
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    }

    movimentacoes = carregar_dados()
    movimentacoes.append(movimentacao)
    salvar_dados(movimentacoes)

    return redirect(url_for("index"))


@app.route("/apagar/<int:indice>")
def apagar_movimentacao(indice):
    movimentacoes = carregar_dados()

    if indice >= 0 and indice < len(movimentacoes):
        movimentacoes.pop(indice)
        salvar_dados(movimentacoes)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

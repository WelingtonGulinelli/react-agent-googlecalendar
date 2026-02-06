from langchain.tools import tool
import re


@tool
def validar_cpf(cpf: str) -> bool:
    """
    Recebe um CPF e valida se é válido ou não.

    Args:
        cpf: str - CPF no formato "XXX.XXX.XXX-XX" ou apenas os números "XXXXXXXXXXX"
    Returns:
        bool - True se o CPF for válido, False caso contrário
    """
    # Remove caracteres não numéricos
    cpf = re.sub(r"\D", "", cpf)

    # Verifica se tem 11 dígitos ou se todos os dígitos são iguais (ex: 111.111.111-11)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto

    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto

    # Verifica se os dígitos calculados conferem com os digitados
    return cpf[-2:] == f"{digito_1}{digito_2}"

# Pergunte o gênero de uma pessoa e válide se é "F" ou "M"
# Se não for "F" ou "M", repita o processo
gender = (input("\033[mQual seu gênero? \033[32m[F / M]\n")).strip().title
while gender != "M" or "F":
    if gender == "Ff":
        print("Seja bem-vinda!")
    elif gender == "Mm":
        print("Seja bem-vindo!")

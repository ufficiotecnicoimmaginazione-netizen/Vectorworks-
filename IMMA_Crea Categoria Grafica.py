import vs

def category_exists(category_name):
    # Utilizza il gestore della classe per iterare attraverso tutte le classi
    class_handle = vs.FActLayer()
    while class_handle != vs.Handle(0):
        class_name = vs.GetClass(class_handle)
        if class_name == category_name:
            return True
        class_handle = vs.NextObj(class_handle)
    return False

def create_category(category_name):
    if not category_exists(category_name):
        vs.NameClass(category_name)
        vs.AlertInform("Categoria Creata", f"La categoria '{category_name}' è stata creata.", True)
    else:
        vs.AlertInform("Categoria Esistente", f"La categoria '{category_name}' esiste già.", False)

def main():
    category_name = "Grafica"
    create_category(category_name)

# Esegui la funzione principale
main()

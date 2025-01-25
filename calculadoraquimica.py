import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors

# Función para calcular propiedades químicas
def calculate_properties(input_molecule):
    try:
        # Intentar cargar como SMILES
        mol = Chem.MolFromSmiles(input_molecule)
        if not mol:
            # Si no funciona, intentar cargar como nombre IUPAC
            mol = Chem.MolFromSmiles(Chem.MolToSmiles(Chem.MolFromInchi(Chem.MolToInchi(mol))))
        
        # Calcular propiedades si la molécula es válida
        if mol:
            molecular_weight = Descriptors.MolWt(mol)
            num_atoms = mol.GetNumAtoms()
            formula = Chem.rdMolDescriptors.CalcMolFormula(mol)
            return {
                "Fórmula molecular": formula,
                "Masa molecular (g/mol)": molecular_weight,
                "Número de átomos": num_atoms,
            }
        else:
            return {"Error": "Entrada inválida. Proporcione un SMILES o nombre IUPAC válido."}
    except Exception as e:
        return {"Error": f"Algo salió mal: {str(e)}"}

# Configuración de la interfaz de Streamlit
st.title("Calculadora Química")
st.write("Ingrese un SMILES o un nombre IUPAC para calcular propiedades básicas.")

# Entrada del usuario
user_input = st.text_input("Entrada (SMILES o nombre IUPAC):")

if user_input:
    # Calcular propiedades
    properties = calculate_properties(user_input)
    # Mostrar resultados
    st.subheader("Resultados")
    for key, value in properties.items():
        st.write(f"**{key}:** {value}")

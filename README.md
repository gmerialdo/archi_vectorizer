\# Archi Vectorizer

Fonctions:
\- PDF -> image
\- nettoyage scan
\- OCR
\- détection murs (Hough)
\- détection pièces
\- API analyse


1) Créer l'environnement Python

linux: 

python3 -m venv venv
source venv/bin/activate

windows:

python -m venv venv
venv\\Scripts\\activate

2) installer les dépendances

pip install -r requirements.txt

Si pytesseract provoque une erreur, il faut aussi installer le moteur OCR système :

Ubuntu :

sudo apt install tesseract-ocr

macOS :

brew install tesseract

Windows :

Télécharger et installer Tesseract OCR officiel : https://github.com/tesseract-ocr/tesseract?utm_source=chatgpt.com 

Puis ajouter le chemin dans Windows si nécessaire :

pytesseract.pytesseract.tesseract\_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)

3) Lancer l’API

Depuis le dossier du projet :

uvicorn app:app --reload

On doit voit quelque chose comme :

INFO: Uvicorn running on http://127.0.0.1:8000

4) Envoyer un PDF scanné

  

Exemple avec curl :

  

curl -X POST ^

\-F "file=@plan.pdf" ^

http://127.0.0.1:8000/analyze

  

6) Lire le résultat

La réponse ressemble à :

{
  "walls":\[
    {
      "start":\[22,120\],
      "end":\[850,120\]
    },
    {
      "start":\[850,120\],
      "end":\[850,620\]
    }
  \],
  "rooms":\[
    {
      "bbox":\[40,50,320,220\]
    }
  \],
  "ocr\_preview":"Cuisine\\nSalle à manger"
}

Interprétation :
walls → segments détectés comme murs potentiels
rooms → zones fermées détectées
ocr\_preview → texte extrait du plan

7) Test plus pratique avec Swagger

FastAPI génère automatiquement une interface :

  

Interface API locale Swagger


Tu peux :
  

ouvrir /docs

cliquer sur POST /analyze

cliquer sur Try it out

sélectionner ton PDF

exécuter

  

Sans ligne de commande.

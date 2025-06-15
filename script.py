# Analisi del sito attuale - Creo un CSV con i problemi identificati
import pandas as pd

# Dati sui problemi del sito attuale
problemi_sito_attuale = {
    'Categoria': [
        'Contenuto',
        'Contenuto', 
        'Contenuto',
        'Design',
        'Design',
        'Funzionalità',
        'Funzionalità',
        'Funzionalità',
        'SEO',
        'SEO',
        'User Experience',
        'User Experience',
        'Marketing',
        'Marketing'
    ],
    'Problema': [
        'Errori grammaticali evidenti (storiaa, nostraaccogliente)',
        'Contenuto troppo generico e poco informativo',
        'Mancanza di informazioni essenziali (menu, prezzi, orari)',
        'Design obsoleto e poco professionale',
        'Assenza di immagini di qualità',
        'Nessun sistema di prenotazione online',
        'Mancanza di integrazione social media',
        'Non ottimizzato per mobile',
        'Mancanza di meta description e title ottimizzati',
        'Struttura URL non SEO-friendly',
        'Navigazione confusa e poco intuitiva',
        'Caricamento lento delle pagine',
        'Assenza di call-to-action efficaci',
        'Mancanza di recensioni e testimonianze'
    ],
    'Impatto_Business': [
        'Alto - Danneggia credibilità e professionalità',
        'Alto - Non convince i visitatori a prenotare',
        'Critico - I clienti non trovano info essenziali',
        'Alto - Prima impressione negativa',
        'Alto - Non stimola appetito e desiderio',
        'Critico - Perdita diretta di prenotazioni',
        'Medio - Mancato engagement e condivisioni',
        'Critico - 70% degli utenti naviga da mobile',
        'Alto - Invisibilità nei motori di ricerca',
        'Medio - Difficoltà nell\'indicizzazione',
        'Alto - Aumenta tasso di abbandono',
        'Alto - 53% utenti abbandona se >3 secondi',
        'Alto - Mancata conversione visitatori in clienti',
        'Medio - Perdita di fiducia e credibilità'
    ],
    'Priorità_Intervento': [
        'Immediata',
        'Alta',
        'Immediata', 
        'Alta',
        'Alta',
        'Immediata',
        'Media',
        'Immediata',
        'Alta',
        'Media',
        'Alta',
        'Alta',
        'Alta',
        'Media'
    ]
}

df_problemi = pd.DataFrame(problemi_sito_attuale)
print("ANALISI PROBLEMI SITO ATTUALE - ANTICO CASALE TRE CAMINI")
print("=" * 60)
print(df_problemi.to_string(index=False))

# Salvo il CSV
df_problemi.to_csv('analisi_problemi_sito_attuale.csv', index=False)
print("\n✅ File salvato: analisi_problemi_sito_attuale.csv")
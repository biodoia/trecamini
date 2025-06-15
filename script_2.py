# Creo un piano di implementazione temporale dettagliato
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

# Piano di implementazione in fasi
piano_implementazione = {
    'Fase': [
        'FASE 1: Analisi e Pianificazione',
        'FASE 1: Analisi e Pianificazione',
        'FASE 1: Analisi e Pianificazione',
        'FASE 1: Analisi e Pianificazione',
        'FASE 2: Design e Contenuti',
        'FASE 2: Design e Contenuti',
        'FASE 2: Design e Contenuti',
        'FASE 2: Design e Contenuti',
        'FASE 3: Sviluppo Tecnico',
        'FASE 3: Sviluppo Tecnico',
        'FASE 3: Sviluppo Tecnico',
        'FASE 3: Sviluppo Tecnico',
        'FASE 4: Integrazione e Testing',
        'FASE 4: Integrazione e Testing',
        'FASE 4: Integrazione e Testing',
        'FASE 5: Lancio e Ottimizzazione',
        'FASE 5: Lancio e Ottimizzazione',
        'FASE 5: Lancio e Ottimizzazione'
    ],
    'Attività': [
        'Audit completo sito attuale',
        'Analisi competitor e benchmark',
        'Definizione architettura informazioni',
        'Pianificazione tecnologie e strumenti',
        'Creazione wireframe e mockup',
        'Servizio fotografico professionale',
        'Redazione contenuti ottimizzati SEO',
        'Progettazione user experience',
        'Setup hosting e CMS',
        'Sviluppo front-end responsive',
        'Integrazione sistemi prenotazione',
        'Implementazione funzionalità avanzate',
        'Testing cross-browser e dispositivi',
        'Integrazione analytics e tracking',
        'Ottimizzazione velocità e SEO',
        'Migrazione contenuti e go-live',
        'Training staff e documentazione',
        'Monitoraggio e prime ottimizzazioni'
    ],
    'Durata_Giorni': [
        5, 3, 4, 3, 
        7, 5, 8, 6,
        4, 12, 8, 10,
        5, 3, 4,
        3, 2, 7
    ],
    'Costo_Stimato': [
        800, 500, 600, 400,
        1500, 2000, 1200, 1800,
        800, 4000, 2500, 3000,
        600, 400, 800,
        500, 300, 800
    ],
    'Responsabile': [
        'Project Manager', 'UX Designer', 'Information Architect', 'Tech Lead',
        'UI Designer', 'Fotografo', 'Copywriter', 'UX Designer',
        'DevOps', 'Frontend Developer', 'Backend Developer', 'Full Stack Developer',
        'QA Tester', 'SEO Specialist', 'Performance Engineer',
        'Project Manager', 'Account Manager', 'Digital Marketing'
    ],
    'Priorità': [
        'Alta', 'Media', 'Alta', 'Alta',
        'Alta', 'Alta', 'Alta', 'Alta',
        'Alta', 'Critica', 'Critica', 'Alta',
        'Alta', 'Alta', 'Alta',
        'Critica', 'Media', 'Alta'
    ]
}

df_piano = pd.DataFrame(piano_implementazione)

print("PIANO DI IMPLEMENTAZIONE - REFACTORING SITO TRE CAMINI")
print("=" * 70)
print(df_piano.to_string(index=False))

# Calcolo tempi e costi totali per fase
fasi_summary = df_piano.groupby('Fase').agg({
    'Durata_Giorni': 'sum',
    'Costo_Stimato': 'sum',
    'Attività': 'count'
}).round(2)

fasi_summary.columns = ['Giorni_Totali', 'Costo_Totale', 'Numero_Attività']

print("\n" + "="*50)
print("RIASSUNTO PER FASE")
print("="*50)
print(fasi_summary.to_string())

print(f"\nTEMPO TOTALE PROGETTO: {df_piano['Durata_Giorni'].sum()} giorni lavorativi (~{df_piano['Durata_Giorni'].sum()//5} settimane)")
print(f"COSTO TOTALE PROGETTO: €{df_piano['Costo_Stimato'].sum():,}")

# Salvo i CSV
df_piano.to_csv('piano_implementazione_dettagliato.csv', index=False)
fasi_summary.to_csv('riassunto_fasi_progetto.csv', index=True)

print("\n✅ File salvati:")
print("- piano_implementazione_dettagliato.csv")
print("- riassunto_fasi_progetto.csv")
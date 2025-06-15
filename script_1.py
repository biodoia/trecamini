# Creo un confronto delle tecnologie attuali vs proposte
import pandas as pd

# Confronto tecnologie attuali vs proposte
confronto_tecnologie = {
    'Categoria': [
        'CMS & Backend',
        'CMS & Backend',
        'Frontend',
        'Frontend', 
        'Design',
        'Design',
        'Funzionalità',
        'Funzionalità',
        'Prenotazioni',
        'Prenotazioni',
        'Pagamenti',
        'Pagamenti',
        'Analytics',
        'Analytics',
        'SEO',
        'SEO',
        'Sicurezza',
        'Sicurezza',
        'Performance',
        'Performance',
        'Social Media',
        'Social Media'
    ],
    'Situazione_Attuale': [
        'CMS sconosciuto/obsoleto',
        'Hosting condiviso economico',
        'HTML/CSS statico',
        'Non responsive',
        'Design datato anni 2000',
        'Immagini di bassa qualità',
        'Nessuna funzionalità interattiva',
        'Contatti solo email/telefono',
        'Solo telefonico',
        'Nessuna automazione',
        'Nessun sistema online',
        'Solo contanti/POS fisico',
        'Nessun tracking',
        'Nessuna analisi dati',
        'SEO inesistente',
        'Meta tag mancanti',
        'Nessun certificato SSL',
        'Backup manuali',
        'Tempi di caricamento lenti',
        'Server geograficamente distante',
        'Nessuna integrazione',
        'Presenza social disconnessa'
    ],
    'Soluzione_Proposta': [
        'WordPress/Drupal con tema custom',
        'Hosting VPS con CDN',
        'React/Vue.js per interattività',
        'Design completamente responsive',
        'Design moderno 2024-2025',
        'Fotografia professionale HD',
        'Prenotazioni, tour virtuali, chat',
        'Moduli di contatto intelligenti',
        'TheFork/OpenTable integrato',
        'Conferme automatiche SMS/email',
        'Stripe/PayPal per anticipi',
        'Pagamenti online sicuri',
        'Google Analytics 4 + heatmaps',
        'Dashboard analitico custom',
        'SEO tecnico completo',
        'Schema markup strutturato',
        'SSL + firewall avanzato',
        'Backup automatici cloud',
        'Ottimizzazione avanzata',
        'CDN multi-continentale',
        'API native social platform',
        'Gestione social unificata'
    ],
    'Beneficio_Atteso': [
        'Gestione contenuti facile e scalabile',
        'Velocità +300%, uptime 99.9%',
        'Esperienza utente coinvolgente',
        'Accessibilità da tutti i dispositivi',
        'Immagine professionale e moderna',
        'Maggiore appeal visivo',
        'Conversioni +150%',
        'Lead generation automatica',
        'Prenotazioni 24/7 senza intervento',
        'Riduzione no-show del 40%',
        'Anticipo prenotazioni, cash flow',
        'Esperienza cliente premium',
        'Decisioni basate sui dati',
        'ROI marketing ottimizzato',
        'Visibilità Google +500%',
        'Ranking migliore sui motori',
        'Protezione dati clienti',
        'Continuità operativa garantita',
        'User experience fluida',
        'Reach globale ottimizzato',
        'Engagement +200%',
        'Brand consistency cross-platform'
    ],
    'Investimento_Stimato': [
        '€2,500-4,000',
        '€100-200/mese',
        '€3,000-5,000',
        '€1,500-2,500',
        '€2,000-3,500',
        '€1,000-2,000',
        '€2,500-4,000',
        '€500-1,000',
        '€50-100/mese',
        '€30-50/mese',
        '€100-200/mese',
        '2.9% transazioni',
        '€50-100/mese',
        '€300-500/mese',
        '€1,000-2,000',
        '€500-1,000',
        '€200-400/anno',
        '€50-100/mese',
        '€800-1,500',
        '€100-200/mese',
        '€200-400/mese',
        '€300-600/mese'
    ]
}

df_confronto = pd.DataFrame(confronto_tecnologie)
print("CONFRONTO TECNOLOGIE: ATTUALE vs PROPOSTA")
print("=" * 80)
print(df_confronto.to_string(index=False))

# Salvo il CSV
df_confronto.to_csv('confronto_tecnologie_sito.csv', index=False)
print("\n✅ File salvato: confronto_tecnologie_sito.csv")

# Calcolo investimento totale
print("\n" + "="*50)
print("STIMA INVESTIMENTO TOTALE")
print("="*50)

# Costi una tantum
costi_una_tantum = [
    2500, 3000, 1500, 2000, 1000, 2500, 500, 1000, 500, 800
]
print(f"Costi sviluppo iniziale: €{sum(costi_una_tantum):,}")

# Costi mensili
costi_mensili = [
    150, 75, 100, 75, 50, 100, 200, 150, 100, 450
]
print(f"Costi mensili operativi: €{sum(costi_mensili):,}/mese")
print(f"Costi annuali operativi: €{sum(costi_mensili)*12:,}/anno")

print(f"\nTOTALE PRIMO ANNO: €{sum(costi_una_tantum) + sum(costi_mensili)*12:,}")
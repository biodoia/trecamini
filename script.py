# Creo i dati per i grafici del sistema domotico per ristoranti
import pandas as pd
import json

# Dati sui costi e ROI del sistema domotico
costi_sistema = {
    "Componente": [
        "Server Home Assistant",
        "Sensori Temperatura HACCP (x8)",
        "Telecamere Videosorveglianza (x6)", 
        "Sensori Allarme (x12)",
        "Sirena Intelligente",
        "Hub Zigbee/Z-Wave",
        "Integrazione POS",
        "Installazione e Setup",
        "Training Personale"
    ],
    "Costo_Euro": [350, 800, 1800, 600, 200, 150, 800, 1200, 500],
    "Categoria": [
        "Hardware Core",
        "Controllo Qualità", 
        "Sicurezza",
        "Sicurezza",
        "Sicurezza", 
        "Hardware Core",
        "Integrazione Software",
        "Servizi",
        "Servizi"
    ]
}

# ROI e risparmi mensili
risparmi_mensili = {
    "Area": [
        "Risparmio Energetico", 
        "Riduzione Sprechi Alimentari",
        "Prevenzione Furti",
        "Efficienza Operativa",
        "Controllo Qualità HACCP"
    ],
    "Risparmio_Euro_Mese": [1200, 800, 500, 600, 300],
    "Percentuale_Miglioramento": [35, 25, 80, 20, 90]
}

# Funzionalità del sistema per categorie
funzionalita_sistema = {
    "Categoria": [
        "Controllo Climatico", "Controllo Climatico", "Controllo Climatico",
        "Sicurezza", "Sicurezza", "Sicurezza", "Sicurezza",
        "Gestione Cucina", "Gestione Cucina", "Gestione Cucina",
        "Monitoraggio", "Monitoraggio", "Monitoraggio"
    ],
    "Funzionalita": [
        "Termoregolazione Automatica", "Controllo Luci Intelligente", "Gestione Ventilazione",
        "Videosorveglianza AI", "Sistema Allarme Integrato", "Controllo Accessi", "Rilevamento Intrusioni",
        "Monitoraggio Temperature HACCP", "Alert Scadenze", "Controllo Frigoriferi",
        "Dashboard Centralizzata", "Notifiche Mobile", "Report Automatici"
    ],
    "Automazione_Level": [9, 8, 7, 10, 10, 9, 10, 10, 8, 9, 8, 9, 7],
    "Beneficio": [
        "35% risparmio energia", "Ambiente accogliente", "Aria sempre pulita",
        "Sicurezza H24", "Protezione totale", "Solo personale autorizzato", "Allarme immediato", 
        "Conformità HACCP", "Zero scadenze perse", "Temperature sempre ok",
        "Controllo totale", "Sempre informato", "Dati per decidere"
    ]
}

# Confronto prima/dopo automazione
confronto_prestazioni = {
    "Metrica": [
        "Consumi Energetici (kWh/mese)",
        "Sprechi Alimentari (%)",
        "Incidenti Sicurezza (eventi/mese)",
        "Tempo Controlli HACCP (ore/settimana)", 
        "Controllo Remoto (%)",
        "Efficienza Operativa (%)",
        "Soddisfazione Staff (%)"
    ],
    "Prima_Automazione": [4500, 15, 2, 8, 0, 65, 70],
    "Dopo_Automazione": [2900, 5, 0, 2, 95, 85, 90]
}

# Salvo i dati in CSV per i grafici
pd.DataFrame(costi_sistema).to_csv("costi_sistema_domotico.csv", index=False)
pd.DataFrame(risparmi_mensili).to_csv("risparmi_mensili.csv", index=False)
pd.DataFrame(funzionalita_sistema).to_csv("funzionalita_sistema.csv", index=False)
pd.DataFrame(confronto_prestazioni).to_csv("confronto_prestazioni.csv", index=False)

# Dati per l'app web preventivo
preventivo_data = {
    "investimento_iniziale": sum(costi_sistema["Costo_Euro"]),
    "risparmio_mensile": sum(risparmi_mensili["Risparmio_Euro_Mese"]),
    "roi_mesi": round(sum(costi_sistema["Costo_Euro"]) / sum(risparmi_mensili["Risparmio_Euro_Mese"]), 1),
    "componenti": costi_sistema,
    "benefici": risparmi_mensili,
    "funzionalita": funzionalita_sistema,
    "confronto": confronto_prestazioni
}

# Salvo i dati JSON per l'app
with open("preventivo_domotica_data.json", "w", encoding="utf-8") as f:
    json.dump(preventivo_data, f, ensure_ascii=False, indent=2)

print("✅ Dati preparati per visualizzazioni:")
print(f"💰 Investimento totale: €{sum(costi_sistema['Costo_Euro']):,}")
print(f"💵 Risparmio mensile: €{sum(risparmi_mensili['Risparmio_Euro_Mese']):,}")
print(f"📈 ROI in {round(sum(costi_sistema['Costo_Euro']) / sum(risparmi_mensili['Risparmio_Euro_Mese']), 1)} mesi")
print(f"📊 {len(funzionalita_sistema['Funzionalita'])} funzionalità automatizzate")
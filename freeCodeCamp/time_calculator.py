def add_time(start, duration, starting_day=None):
    # Definizione dell'ordine dei giorni per calcolare l'offset
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    # 1. Parsing dell'ora di inizio
    time, am_pm = start.split()
    hour_str, minute_str = time.split(':')
    current_hour = int(hour_str)
    current_minute = int(minute_str)

    # Converti l'ora di inizio in minuti totali (dal lunedì)
    # 12 PM (mezzogiorno) è 12. 12 AM (mezzanotte) è 0.
    if am_pm == 'PM' and current_hour != 12:
        current_hour += 12
    elif am_pm == 'AM' and current_hour == 12:
        current_hour = 0
    
    start_minutes = (current_hour * 60) + current_minute

    # 2. Parsing della durata e conversione in minuti
    duration_hour, duration_minute = duration.split(':')
    duration_minutes = (int(duration_hour) * 60) + int(duration_minute)
    
    # 3. Calcolo del tempo finale (in minuti totali)
    total_minutes = start_minutes + duration_minutes

    # 4. Calcolo del giorno, ora e minuti finali
    minutes_in_a_day = 24 * 60
    
    # Calcola il numero di giorni passati
    days_later = total_minutes // minutes_in_a_day
    
    # Calcola i minuti rimanenti entro il giorno
    final_minutes_of_day = total_minutes % minutes_in_a_day

    # Calcola l'ora finale in formato 24 ore
    final_hour_24 = final_minutes_of_day // 60
    final_minute = final_minutes_of_day % 60

    # 5. Conversione in formato 12 ore e AM/PM
    
    # Determina l'indicatore AM/PM finale
    if final_hour_24 >= 12:
        new_am_pm = 'PM'
    else:
        new_am_pm = 'AM'

    # Converte l'ora da 24 a 12 ore
    if final_hour_24 > 12:
        final_hour_12 = final_hour_24 - 12
    elif final_hour_24 == 0:
        final_hour_12 = 12 # 00:XX diventa 12:XX AM
    else:
        final_hour_12 = final_hour_24
        
    final_minute_str = str(final_minute).zfill(2)
    
    # 6. Costruzione della stringa base dell'ora
    new_time = f"{final_hour_12}:{final_minute_str} {new_am_pm}"

    # 7. Gestione del giorno della settimana
    if starting_day:
        # Normalizza la capitalizzazione del giorno di partenza per il lookup
        starting_day_lower = starting_day.lower()
        
        # Trova l'indice del giorno di partenza e calcola l'indice del giorno finale
        try:
            start_index = days_of_week.index(starting_day_lower)
            final_index = (start_index + days_later) % 7
            
            # Capitalizza il giorno finale correttamente (es. Tuesday)
            final_day = days_of_week[final_index].capitalize()
            
            new_time += f", {final_day}"
        except ValueError:
            # Questo gestisce il caso in cui il giorno di partenza non sia valido
            # (anche se i test FreeCodeCamp di solito garantiscono input validi)
            pass 

    # 8. Aggiunta dell'indicatore 'days later'
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'
        
    return new_time

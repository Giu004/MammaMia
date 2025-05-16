importa json
richieste di importazione
da urllib.parse importa urlparse

def get_domains(pastebin_url):
    """
    Recupera il contenuto del Pastebin con i domini.
    :param pastebin_url: URL del Pastebin da cui recuperare i domini.
    :return: Lista dei domini dal file Pastebin.
    """
    Tentativo:
        risposta = richieste.get(pastebin_url)
        risposta.aumenta_per_stato()
        domini = response.text.strip().split('\n')
        domini = [domain.strip().replace('\r', '') per dominio in domini]
        domini di ritorno
    eccetto requests.RequestException come e:
        print(f"Errore durante il recupero dei domini: {e}")
        ritorno []

def extract_full_domain(dominio, chiave_sito):
    """
    Estrai il dominio completo da un URL con https:// e www. per Tantifilm e StreamingWatch,
    mentre per gli altri solo con https://.
    :param dominio: Dominio da analizzare.
    :param site_key: Nome del sito per decidere il prefisso.
    :return: Dominio completo con schema e www. se richiesto.
    """
    parsed_url = urlparse(dominio)
    schema = parsed_url.scheme se parsed_url.scheme altrimenti 'https'
    netloc = parsed_url.netloc o parsed_url.path

    se site_key in ['Tantifilm', 'StreamingWatch']:
        se non netloc.startswith('www.'):
            netloc = 'www.' + netloc
        restituisci f"https://{netloc}"
    altro:
        restituisci f"https://{netloc}"

def check_redirect(dominio, chiave_sito):
    """
    Verifica se un dominio fa un reindirizzamento e restituisce il dominio finale completo con https:// e www.
    :param dominio: Dominio da verificare.
    :param site_key: Nome del sito per decidere il prefisso.
    :return: Tuple con l'URL originale e il dominio finale completo.
    """
    se non domain.startswith(('http://', ​​'https://')):
        dominio = 'http://' + dominio

    Tentativo:
        response = requests.get(domain, allow_redirects=True, verify=False) # Disabilita la verifica SSL
        final_url = response.url
        dominio_finale = estrai_dominio_completo(URL_finale, chiave_sito)
        dominio di ritorno, dominio_finale
    eccetto requests.RequestException come e:
        restituisci dominio, f"Errore: {str(e)}"

def update_json_file():
    """
    Aggiorna il file JSON con i domini finali (post-redirect) recuperati da Pastebin.
    """
    Tentativo:
        con open('config.json', 'r', encoding='utf-8') come file:
            dati = json.load(file)
    eccetto FileNotFoundError:
        print("Errore: Il file config.json non è stato trovato.")
        ritorno
    eccetto json.JSONDecodeError:
        print("Errore: Il file config.json non è un JSON valido.")
        ritorno

    streamingcommunity_url = 'https://pastebin.com/raw/KgQ4jTy6'
    streamingcommunity_domains = get_domains(streamingcommunity_url)

    general_pastebin_url = 'https://pastebin.com/raw/E8WAhekV'
    domini_generali = ottieni_domini(general_pastebin_url)

    se non general_domains o non streamingcommunity_domains:
        print("Lista dei domini vuota. Controlla i link di Pastebin.")
        ritorno

    mappatura_del_sito = {
        'StreamingCommunity': streamingcommunity_domains[0],
        'Filmpertutti': general_domains[1],
        'Tantifilm': general_domains[2],
        'LordChannel': general_domains[3],
        'StreamingWatch': general_domains[4],
        'CB01': domini_generali[5],
        'DDLStream': domini_generali[6],
        'Guardaserie': general_domains[7],
        'GuardaHD': general_domains[8],
        'AnimeWorld': general_domains[9],
        'SkyStreaming': general_domains[10],
        'DaddyLiveHD': domini_generali[11],
    }

    per site_key, domain_url in site_mapping.items():
        se site_key in data['Siti']:
            originale, final_domain = check_redirect(domain_url, site_key)
            se "Errore" in final_domain:
                print(f"Errore nel reindirizzamento di {original}: {final_domain}")
                continuare
            dati['Siti'][chiave_sito]['url'] = dominio_finale
            print(f"Aggiornato {site_key}: {final_domain}")

    Tentativo:
        con open('config.json', 'w', encoding='utf-8') come file:
            json.dump(dati, file, rientro=4, ensure_ascii=False)
        print("File config.json aggiornato con successo!")
    eccetto Eccezione come e:
        print(f"Errore durante il salvataggio del file JSON: {e}")

se __name__ == '__main__':
    aggiorna_file_json()

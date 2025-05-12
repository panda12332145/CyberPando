from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
import requests
import time
import socket
import random
import os

console = Console()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_credits():
    clear_screen()
    credit_text = '''
    [bold green]==================== Créditos ====================[/bold green]

    [bold cyan]Criadores:[/bold cyan]

    [bold yellow]💻 Douglas Nunes[/bold yellow]
    - GitHub:https://github.com/NunesGunnar
    - LinkedIn: https://www.linkedin.com/in/douglas-nunes-0176672a0/
    - Instagram: https://www.instagram.com/winner_2s

    [bold yellow]🐼 panda12332145[/bold yellow]
    - GitHub: https://github.com/panda12332145
    - LinkedIn: https://www.linkedin.com/in/athos-d%C3%A3-boanergis-5585a4288/
    - Site: https://panda-h0me.netlify.app/
    - YouTube: https://www.youtube.com/@X86BinaryGhost
    - Instagram: https://www.instagram.com/01pandal10/
    [bold green]=================================================[/bold green]
    '''
    console.print(credit_text)

def format_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    return url

def get_ip_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        if response.status_code == 200:
            data = response.json()
            info = {
                'IP': data.get('query'),
                'Cidade': data.get('city'),
                'Região': data.get('regionName'),
                'País': data.get('country'),
                'Organização': data.get('org'),
                'ISP': data.get('isp'),
                'Latitude': data.get('lat'),
                'Longitude': data.get('lon')
            }
            return info
        else:
            return {'Erro': 'Não foi possível obter informações do IP.'}
    except Exception as e:
        return {'Erro': str(e)}

def check_link(url):
    url = format_url(url)
    try:
        response = requests.get(url)
        ip_address = socket.gethostbyname(url.replace('http://', '').replace('https://', '').split('/')[0])
        
        if response.status_code == 200:
            ip_info = get_ip_info(ip_address)
            return f'Link [bold green]{url}[/bold green] está acessível!\n' + \
                   f'[bold cyan]IP:[/bold cyan] {ip_address}\n' + \
                   f'[bold cyan]Informações do IP:[/bold cyan] {ip_info}\n' + \
                   f'[bold green]Nunca clique em links encurtados ou estranhos sem antes verificar com uma ferramenta como [bold white]virustotal.com[bold white][bold green].[bold green]'
        else:
            return f'Link [bold red]{url}[/bold red] retornou status {response.status_code}.'
    except requests.exceptions.RequestException as e:
        return f'Erro ao verificar [bold red]{url}[/bold red]: {e}'

def main_menu():
    clear_screen()
    while(True):
        banner1 = Text(''''
 ▄████▄ ▓██   ██▓ ▄▄▄▄    ▓█████ ██▀███   ██▓███   ▄▄▄      ███▄    █  ▓█████▄  ▒█████  
▒██▀ ▀█  ▒██  ██▒▓█████▄  ▓█   ▀▓██ ▒ ██▒▓██░  ██ ▒████▄    ██ ▀█   █  ▒██▀ ██▌▒██▒  ██▒
▒▓█    ▄  ▒██ ██░▒██▒ ▄██ ▒███  ▓██ ░▄█ ▒▓██░ ██▓▒▒██  ▀█▄ ▓██  ▀█ ██▒ ░██   █▌▒██░  ██▒
▒▓▓▄ ▄██  ░ ▐██▓░▒██░█▀   ▒▓█  ▄▒██▀▀█▄  ▒██▄█▓▒ ▒░██▄▄▄▄██▓██▒  ▐▌██▒▒░▓█▄   ▌▒██   ██░
▒ ▓███▀   ░ ██▒▓░░▓█  ▀█▓▒░▒████░██▓ ▒██▒▒██▒ ░  ░▒▓█   ▓██▒██░   ▓██░░░▒████▓ ░ ████▓▒░
░ ░▒ ▒     ██▒▒▒ ░▒▓███▀▒░░░ ▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░▒▒   ▓▒█░ ▒░   ▒ ▒ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ 
  ░  ▒   ▓██ ░▒░ ▒░▒   ░ ░ ░ ░    ░▒ ░ ▒ ░▒ ░     ░ ░   ▒▒ ░ ░░   ░ ▒░  ░ ▒  ▒   ░ ▒ ▒░ 
░        ▒ ▒ ░░   ░    ░     ░    ░░   ░ ░░         ░   ▒     ░   ░ ░   ░ ░  ░ ░ ░ ░ ▒  
░ ░      ░ ░      ░      ░   ░     ░                    ░           ░     ░        ░ ░  
    ''', style="bold cyan")

        banner2 = Text('''
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║
╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║     ██║  ██║██║ ╚████║██████╔╝╚██████╔╝
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 
    ''', style="bold green")

        banner = banner1 if random.randint(1, 2) == 1 else banner2
        console.print(banner)
        console.print(Panel("Olá, me chamo [bold magenta]CyberPanDo[/bold magenta]! Meu objetivo é ajudar você com dúvidas sobre [bold red]segurança digital[/bold red].",
                             title="👾 [bold green]Bem-vindo[/bold green]", border_style="green"))
        
        table = Table(title="Escolha uma opção:", show_header=True, header_style="bold green")
        table.add_column("Opção", style="cyan")
        table.add_column("Descrição", style="magenta")
        
        table.add_row("0", "Sair")
        table.add_row("1", "Dúvida com Email")
        table.add_row("2", "Dúvida com Site")
        table.add_row("3", "Dúvida com Link")
        table.add_row("4", "Objetos achados bootáveis")
        table.add_row("5", "O que fazer em caso de ransomware")
        table.add_row("6", "Créditos do Programa")
        
        console.print(table)

        opcao = console.input("[bold yellow]Digite aqui sua dúvida (0 a 6): [/bold yellow] ")

        if opcao == "0":
            console.print(Panel("[bold red]Saindo do programa...[/bold red]", border_style="bright_red"))
            time.sleep(2.30)
            clear_screen()
            break

        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
        ) as progress:
            task = progress.add_task("[cyan]Carregando...", total=100)
            while not progress.finished:
                progress.update(task, advance=1)
                time.sleep(0.05)

        if opcao == "1":
            console.print(Panel("[bold green] Cuidado com e-mails de remetentes desconhecidos, com anexos ou links suspeitos.[/bold green]\n"
                                "Nunca clique sem verificar o domínio e evite baixar arquivos não solicitados.",
                                title="📧 Dúvida com Email", border_style="bright_green"))
            time.sleep(5.00)
            clear_screen()
        elif opcao == "2":
            console.print(Panel("[bold blue] Verifique se o site usa HTTPS e confira se o endereço é legítimo.[/bold blue]\n"
                                "Desconfie de erros de digitação no nome ou design malfeito.",
                                title="🌐 Dúvida com Site", border_style="bright_blue"))
            time.sleep(5.00)
            clear_screen()
        elif opcao == "3":
            link = console.input("[bold yellow]Digite o link que deseja verificar: [/bold yellow]")
            result = check_link(link)
            console.print(Panel(result, title="🔗 Resultado da Verificação", border_style="bright_magenta"))
            time.sleep(5.00)
            clear_screen()
        elif opcao == "4":
            console.print(Panel("[bold red] Dispositivos desconhecidos (como pendrives encontrados na rua) podem conter malware.[/bold red]\n"
                                "Nunca conecte dispositivos sem saber a procedência — isso é uma isca comum usada por atacantes.",
                                title="💾 Objetos Bootáveis", border_style="bright_red"))
            time.sleep(5.00)
            clear_screen()
        elif opcao == "5":
            console.print(Panel("[bold yellow]⚠ O que fazer se você cair em um ransomware:[/bold yellow]\n"
                                "1. Desconecte imediatamente seu dispositivo da internet.\n"
                                "2. Desligue o computador para evitar que o ransomware se espalhe.\n"
                                "3. Verifique se você tem backups atualizados e restauráveis.\n"
                                "4. Não pague o resgate! Isso não garante a recuperação dos arquivos.\n"
                                "5. Use ferramentas de remoção de ransomware, como Malwarebytes ou HitmanPro.\n"
                                "6. Denuncie à polícia e autoridades competentes.\n"
                                "7. Restaure seus arquivos a partir de backups, se possível, e reforce as defesas do sistema.",
                                title="🛡️ Ransomware", border_style="bright_yellow"))
            time.sleep(5.00)
            clear_screen()
        elif opcao == "6":
            show_credits()
            time.sleep(10.35)
            clear_screen()

        else:
            console.print(Panel("[bold red]Opção inválida. Tente novamente digitando um número de 0 a 5.[/bold red]", border_style="bright_red"))
            time.sleep(5.00)
            clear_screen()

if __name__ == "__main__":
    main_menu()

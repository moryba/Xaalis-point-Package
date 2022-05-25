import subprocess
import webbrowser
import time

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def program_start():
    
        sanctions = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND OFAC OR Cuba OR Iran OR “North Korea” OR Sudan OR Syria OR “South Sudan” OR Crimea OR Russia OR Burma OR Myanmar" )

        Litigation = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND court OR case OR defendant OR plaintiff OR suspect OR dispute OR litigation OR suit OR restitution OR indict OR accuse OR convict OR prosecute OR “legal action” OR investigate OR judgement OR “legal proceeding” OR sue OR lawsuit OR mistrial OR perjury" )

        Other_Risky_Categories  = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND antitrust OR hijack OR bribe OR corruption OR counterfeit OR embezzle OR endangerment OR extort OR RICO OR racketeering OR forgery OR fraud OR “insider trading” OR “money launder” ")
                                                              
        Other_Risky_Categories12  = webbrowser.get('edge').open('https://www.google.com/search?q=' + search +  " AND ponzi OR “tax evasion” OR terrorism OR “terrorism financing” OR smuggle OR trafficking OR WMD OR “weapon of mass destruction” OR “organized crime” OR “elder abuse” ")

        Other_Risky_Categories2 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND manipulate OR kidnap OR firearm OR prostitute OR “online betting” OR “financial crime” OR narcotic OR “market manipulate” ")

        Reputational_Categories =  webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND arson OR assault OR pornography OR conspiracy OR “child abuse” OR espionage OR explosive OR “false advertising” OR murder OR rape OR piracy OR “forced labour” OR “price manipulation” OR burglary") 
                                                               
        Reputational_Categories12 =  webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND larceny OR loot OR theft OR shoplift OR gamble OR “crimes against humanity” OR “environmental crime” OR “interstate commerce” OR suspension OR “stolen property”  AND “War Crime” ")

        NegativeMedia1 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND abuse OR apprehend OR accuse OR acquit OR allege OR arrest OR bankrupt OR breach OR cartel OR contraband OR crime OR criminal OR deception OR defraud OR detain OR discipline")
                                                    
        NegativeMedia12 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND  discriminate OR disqualify OR drug OR embezzle OR extort OR false OR felony OR fine OR fugitive OR illegal OR illicit OR imprison OR improper OR jail OR kickback")

        NegativeMedia2 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND misconduct OR misappropriate OR narcotic OR negligence OR offense OR prohibit OR prosecute OR revoke OR sanction OR scam OR scandal OR swindle OR sexual OR terror OR unethical OR “unfair practice” ")
                                                     
        NegativeMedia22 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search +  " AND unlawful Or verdict OR victim OR violate OR “arrest warrant” OR weapon OR penalty OR “financial problem” OR interrogate OR judgement OR libel OR malpractice OR misuse")

        NegativeMedia3 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND punish OR crony OR insolvent OR “asset freezing” OR assault OR irregular OR mob OR suspicion OR “pyramid scheme” OR liability OR wrongdoing OR FCPA OR conflict OR embargo")
                                                     
        NegativeMedia32 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search +  " AND settle OR arraign attack OR armament OR banned OR banning OR blacklist OR cocaine OR deforestation OR deposed OR defamation OR extradition OR derogatory OR “diamond trading” OR falsify")

        NegativeMedia4 = webbrowser.get('edge').open('https://www.google.com/search?q=' + search + " AND gang OR guilty OR harassment OR homicide OR persecute OR probation OR ransom OR smuggle OR hacker OR hacking OR treason OR liquidation OR mafia")
        return sanctions, Litigation, Other_Risky_Categories, Other_Risky_Categories12, Other_Risky_Categories2, Reputational_Categories, Reputational_Categories12, NegativeMedia1, NegativeMedia12, NegativeMedia2, NegativeMedia22, NegativeMedia3, NegativeMedia32, NegativeMedia4  
        


steps = ['round1', 'round2', 'round3', 'round4', 'round5', 'round6', 'round7', 'round8', 'round9', 'round10', 'round11', 'round12', 'round13', 'round14', 'round15']

for i in steps:
    search = input("Please, give a variable: ")
    search = search.replace("&","%26")
    search = search.replace("+", "%2B")
    time.sleep(1.5)
    if search.lower() == "no":
        print("Thanks, see you next time")
        time.sleep(1.9)
        break
    else:
        subprocess.Popen(edge_path)
        time.sleep(1.5)
        program_start()
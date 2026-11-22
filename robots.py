import requests

def find_sitemap(robots):
    """ 
    Finds the sitemap on the robots.txt page
    """ 
    for line in robots.splitlines():

        if "Sitemap" in line:

            return line[line.find("https"):]

    return None

def find_robots(url):
    """
    Returns the robots.txt page for the current webbsite
    """  
    try:

        session = requests.session()
        page    = session.get(url+"/robots.txt")
        
        return page.text
    
    except:
        return None

def find_allow_disallow_list(robots):
    """
    Finds the allow and disallow lists for the current website
    """  
    disallow = list()
    allow    = list()
    agent_found = False

    for line in robots.splitlines():

        if("User-agent" in line):

            if "*" in line:

                agent_found = True

            else:

                agent_found = False
                
        if "Allow" in line and agent_found:

            allow.append(line[line.find("/"):])

        if "Disallow" in line and agent_found:

            disallow.append(line[line.find("/"):])

    return allow,disallow

def find_crawl_delay(robots):
    """
    Finds the crawl delay for the current website
    """  
    delay       = 10
    agent_found = False

    for line in robots.splitlines():

        if ("User-agent" in line and "*" in line):

            agent_found = True

        if("Crawl-Delay" in line and agent_found):

            delay  = line[line.find["[":(len(line)-1)]]
            
            return delay

    return delay
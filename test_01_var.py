#diferent variable
url = "https://leetcode.com/RL_ukr/"
testLogin = "RL_ukr"
sHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
# objResponseWebPage = requests.get(url, headers=sHeaders)
html_doc_Example = """
                <html>
                    <head><title>Test Login_from current file</title></head>
                    <body>
                        <div data-title="0:data-title"><b>01:title story</b></div>
                        <p data-title="p-title"><b>title story</b></p>

                        <p class="story">Once upon a time there were three little sisters; and their names were
                            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
                            and
                            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                            and they lived at the bottom of a well.
                        </p>
                        
                        <div>1:Simly Test1 div</div>
                        <div>2:Simly Test2 div</div>

                        <div class="title_3">3:Mitten Test3 div</div>
                        <div class="title_4">4:Mitten Test4 div</div>

                        <div data-title="data-title1">5:div data-title1</div>
                        <div data-title="data-title2">6:div data-title2</div>
                        <div data-title="data-title3">7:div data-title3</div>

                        <div data-title="8:Investments in 2016" class="flex flex-1 justify-between">
                            <span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">
                                9:Investments in 2016
                            </span>
                            <span class="text-label-3 dark:text-dark-label-3 lc-md:inline hidden whitespace-nowrap">
                                10:a month ago
                            </span>
                        </div>
                        <div data-title="11:Department Highest Salary" class="flex flex-1 justify-between">
                            <span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">
                                12:Department Highest Salary
                            </span>
                            <span class="text-label-3 dark:text-dark-label-3 lc-md:inline hidden whitespace-nowrap">
                                13:a month ago
                            </span>
                        </div>
                    </body>
                </html>
                
                

                <p class="story">...</p>
            """
#-------------    # python scraper.py -h  -> help    
# scraper.py [-h] [-d DOMAIN] [-u USER]
# python scraper.py -h    
# python scraper.py -d selenium -u RL_ukr
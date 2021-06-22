from telethon import TelegramClient
import os
import time

api_id = 3920158 
api_hash = '0cfc2f8dfef6db13d138a31192b18935'
client = TelegramClient('lpssxs', api_id , api_hash)

async def main():

    me = await client.get_me()
    
    #TuringLabbot
    
    #种豆提交
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"种豆提交,waiting")
    await client.send_message('@TuringLabbot','/submit_activity_codes bean olmijoxgmjutyjqjygcacges7ijukkf4wuebt6i&xmblfgd3rmwo5za7i4mfalb6pfmn7nshle5syba&olmijoxgmjuty75bgjnimacr5g2lv75haxkxwji')
    time.sleep(5)
    
     #农场提交
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"农场提交,waiting")
    await client.send_message('@TuringLabbot','/submit_activity_codes farm 26c6b461fba74eae8764b99a7ccabc81&13c59d475d634464a3956d8a117ec05e&b4f5320897994c1cb7b572d694dd363b')
    time.sleep(5)

     #萌宠提交
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"萌宠提交,waiting")
    await client.send_message('@TuringLabbot','/submit_activity_codes pet MTAxODc2NTEzMDAwMDAwMDAyMDY2ODczNQ==&MTEzMzI0OTE0NTAwMDAwMDA0MjY1NDAwNQ==&MTE1NDUwMTI0MDAwMDAwMDQ2NzE2ODk5')
    time.sleep(5)

     #京喜工厂提交    
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"京喜工厂提交,waiting")
    await client.send_message('@TuringLabbot','/submit_activity_codes jxfactory {"smp":"0a83f30ec0562e33e428eefd0b50b98e","active":"jdnc_1_sxhuasheng210305_2","joinnum":1}&{"smp":"1b559d440f856408d7787940c68996b3","active":"jdnc_1_caomi210305_2","joinnum":1}&{"smp":"e83664e3f03425774fc65ff80669b992","active":"jdnc_1_sxhuasheng210305_2","joinnum":1}')
    time.sleep(5)    

     #东东工厂提交 
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"东东工厂提交,waiting")
    await client.send_message('@TuringLabbot','/submit_activity_codes ddfactory P04z54XCjVWnYaS5m9cZ2b8j3lLlJH094OnC9I&P04z54XCjVWnYaS5m9cZzKkpycg9OettKcmdw&T0225KkcRhxK_FHUdB7zkv9eJgCjVWnYaS5kRrbA')
    time.sleep(5)


    
    #LvanLamCommitCodeBot
    
    #jd_cash
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"jd_cash submit ,waiting")
    await client.send_message('@LvanLamCommitCodeBot','/jdcash eU9YaujgY_0nom7SmSJB0g&eU9YPrDIPZZHjzmwtwVU&eU9Yau7hb_klpWrSzXtHhA')
    time.sleep(5)
    
    #jd_jdzz
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"jd_jdzz submit ,waiting")
    await client.send_message('@LvanLamCommitCodeBot','/jdzz S5KkcRhpL8FXWcxrzxqZYcA&S5KkcEkJjrj62Xk2R6IFN&S5KkcRhxK_FHUdB7zkv9eJg')
    time.sleep(5)

    #jd_jdcrazyjoy
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"jd_jdcrazyjoy submit ,waiting")
    await client.send_message('@LvanLamCommitCodeBot','/jdcrazyjoy eo5lf9mPzsGLoqgTlmN-AKt9zd5YaBeE&sEaeCDtGdUB_VFRCJhMp7A==&JDajqIExihJ_1fAyY7YRsKt9zd5YaBeE')

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"All Sharecode is submited , thank you !")

with client:
	
	client.loop.run_until_complete(main())



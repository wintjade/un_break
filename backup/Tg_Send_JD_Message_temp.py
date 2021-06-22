from telethon import TelegramClient
import os
import time

api_id = 3920158 
api_hash = '0cfc2f8dfef6db13d138a31192b18935'
client = TelegramClient('lpssxs', api_id , api_hash)

async def main():

    me = await client.get_me()
    
    #TuringLabbot - temp
    
    #sgmh 盲盒
    await client.send_message('@TuringLabbot','/submit_activity_codes sgmh T0225KkcRhpL8FXWcxrzxqZYcACjVQmoaT5kRrbA&T0205KkcEkJjrj62Xk2R6IFNCjVQmoaT5kRrbA&T0225KkcRhxK_FHUdB7zkv9eJgCjVQmoaT5kRrbA')
    time.sleep(5)
    
     #jxcfd 财富岛
    await client.send_message('@TuringLabbot','/submit_activity_codes jxcfd 94180BA0783DCC197307D2832976E6CE3201B3D7BEA70454886A058CCB503799&9F9592AA9EA22D2D2F83DE0D0FD748C4C9DEC1CDEA7992A9896D48B5E0494FA4&46FBABC03B147B530196D4BA30850C5AF157C48C68D5B2A917B721C0B48CDE1E')
    time.sleep(5)

     #jdglobal 环球挑战 
    await client.send_message('@TuringLabbot','/submit_activity_codes jdglobal ZTA1ZmVSVm1QWTB2YURlMkhhOUFmSUxseEZLakx4Y0JuTnUxb2d4TEFqST0=&MzIyYXpNVTJ1aDQ3Z09sb2xDWjh3dz09&RmxaR3JNS2ZqK2RwZDEybTVHOXl5MGVWb0VXY0ZzaEptaGdpUHlad0hFTT0=')
    time.sleep(5)


with client:
	
	client.loop.run_until_complete(main())



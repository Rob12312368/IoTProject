import time, random, requests, datetime
import DAN

#ServerURL = 'https://demo.iottalk.tw'      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
#ServerURL = 'http://iottalk.imslab.org'
ServerURL = 'http://iottalk.ncku.edu.tw'
Reg_addr = 'mytest' #if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control']
DAN.profile['d_name']= 'change2' 

#DAN.register_device(Reg_addr)
DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

while True:
    try:
        currentHour = datetime.datetime.now().hour
        IDF_data = random.uniform(1, 10)
        DAN.push ('Dummy_Sensor', IDF_data) #Push data to an input device feature "Dummy_Sensor"

        #==================================

        ODF_data = DAN.pull('Dummy_Control')#Pull data from an output device feature "Dummy_Control"
        if ODF_data != None:
            print(ODF_data[0])

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(0.2)


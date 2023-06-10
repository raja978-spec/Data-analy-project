from django.db import connection
from django.shortcuts import render,redirect
from .models import DashBoard
import json
 
# Scrape the data from json file and put it on 
# DashBoard database
def Putter(request):
    global inten,like,rele,Syea,Eyea,coun,top,reg,url,add,pub,Insi,msg
    if(request.method=="POST"):
        File=open('NewsLetter/jsondata.json',encoding='utf8')
        Data=json.load(File)
        for i in range(len(Data)):  
            if (Data[i]['intensity'] != " "):
                inten=Data[i]['intensity']
            if (Data[i]['likelihood'] != " "):
                like=Data[i]['likelihood']

            if (Data[i]["relevance"] != " "):
               rele=Data[i]["relevance"]
 
            if (Data[i]['start_year'] != " "):
               Syea=Data[i]['start_year']
     
            if (Data[i]['end_year'] != " "):
               Eyea=Data[i]['end_year']
 
            if (Data[i]['country'] != " "):
               coun=Data[i]['country']

            if (Data[i]['topic'] != " "):
              top=Data[i]['topic']

            if (Data[i]['region'] != " "):
              reg=Data[i]['region']

            if (Data[i]['url'] != " "):
               url=Data[i]['url']

            if (Data[i]['added'] != " "):
              add=Data[i]['added']
        
            if (Data[i]['published'] != " "):
               pub=Data[i]['published']
        
            if (Data[i]['insight'] != " "):
               Insi=Data[i]['insight']                           
            
            obj=DashBoard.objects.create(Intensity=inten,
                                         Likehood=like,
                                         Relevance=rele,
                                         SYear=Syea,
                                         EYear=Eyea,
                                         Country=coun,
                                         Topic=top,
                                         Region=reg,
                                         Url=url,
                                         Added=add,
                                         Published=pub,
                                         Insight=Insi
                                         )
        msg=0
        if(msg==0):
            obj.save()
            msg=1
        if(msg==1):
            return render(request,'index.html',{'data':"Data Inserted"})
        if(msg==0):
            return render(request,'index.html')
    return render(request,'index.html')


# For GET request it gives 500 data from the 1000 data of
# database, gives data to Country wise likelihood, Topic
# wise relevance, percentage for Relevance, Likelihood
# intensity 
def dashBoard(request):
   obj=DashBoard.objects.all()[:500]   
   n_news=DashBoard.objects.all()
   
   # These three gives the data for Percentage of L,R,I chart
   likehood_data=[]
   intensity_data=[]
   relevance_data=[]
   
   # These two gives data to Country wise Likelihood,Topic wise news relevance
   # charts 
   countrywise_likelihood_data=[]
   countrywise_relevance_data=[]

   
   cursor=connection.cursor()
   country={i['Country'] for i in DashBoard.objects.values('Country') if i != " "}
   topics={i['Topic'] for i in DashBoard.objects.values('Topic') if i != " "}
   
   fc=[i for i in country][:11]
   ft=[i for i in topics][:11]
   
   
   
   # These two cursor takes likelihood and sum of relevance
   # for ountry wise Likelihood,Topic wise news relevance
   # charts 
   for i in country:
      cursor.execute(f'select Sum(Likehood) from NewsLetter_dashboard where Country="{i}"')
      countrywise_likelihood_data.append(cursor.fetchone())
   
   for j in topics:
      cursor.execute(f'select Sum(Relevance) from NewsLetter_dashboard where Topic="{j}"')
      countrywise_relevance_data.append(cursor.fetchone())

   
   
   # These three cursor take's data from database for Percentage of L,R,I chart
   cursor.execute(f'select Sum(Likehood) from NewsLetter_dashboard ')
   likehood_data.append(cursor.fetchone())
   
   cursor.execute(f'select Sum(Intensity) from NewsLetter_dashboard')
   intensity_data.append(cursor.fetchone())
   
   cursor.execute(f'select Sum(Relevance) from NewsLetter_dashboard')
   relevance_data.append(cursor.fetchone())
   
   
   # Cursor gives the data as list of tuples EX: [(),()]
   # Below five statements format the data as List
   # EX: [ele1,ele2]
   fl=[likehood_data[i][0] for i in range(len(likehood_data))]
   formated_inten=[intensity_data[i][0] for i in range(len(intensity_data))]
   formated_rele=[relevance_data[i][0] for i in range(len(relevance_data))]
   formated_likelihood_country_data=[countrywise_likelihood_data[i][0] for i in range(len(countrywise_likelihood_data))][:10] 
   formated_relevance_country_data=[countrywise_relevance_data[i][0] for i in range(len(countrywise_relevance_data))][:10]
   
   
   # Below condition statement are helps to make filter in 
   # DashBoard
   if (request.method=="POST"):
       Fill=request.POST['fil'] 
       Data=DashBoard.objects.filter(EYear=Fill) | DashBoard.objects.filter(Topic=Fill) | DashBoard.objects.filter(Region=Fill) | DashBoard.objects.filter(Country=Fill)
      
	  # Returns the reterived data as dict format to html page
       return render(request,'index.html',{'topic':ft,'frcd':formated_relevance_country_data,'country':fc,'flcd':formated_likelihood_country_data,'likehood':fl[0],'relevance':formated_rele[0],'intensity':formated_inten[0],'totalnews':len(n_news),'totalcountry':len(country),'msg':"Result for "+Fill,'data':Data})
   
   #Returns the reterived data as dict format to html page
   return render(request,'index.html',{'topic':ft,'frcd':formated_relevance_country_data,'country':fc,'flcd':formated_likelihood_country_data,'likehood':fl[0],'relevance':formated_rele[0],'intensity':formated_inten[0],'totalnews':len(n_news),'totalcountry':len(country),'data':obj})








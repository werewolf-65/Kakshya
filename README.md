An information-oriented social network designed for student 
organizations 



1. Start server with:
	
   python manage.py runserver 

2. To run the chat section, 

   you may have to run redis on docker 

   for that,type: ./dockerrun.tex 

3. For the Elasticsearch integration,

   download the elasticsearch package at https://www.elastic.co/downloads/elasticsearch

   the version we're using is: 6.6.0 but it may work alright in the newer versions

   for rebuilding the search indexes, you'll need to run the command:

   python manage.py search_index --rebuild 

   run ./elasticsearch from the downloaded package before trying out the 'search' feature. 




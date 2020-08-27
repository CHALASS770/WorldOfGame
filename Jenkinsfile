pipeline {
   agent any

   stages {
      stage('checkout')
      {
         steps{
         git "https://github.com/CHALASS770/WorldOfGame.git"
            }
      }
      
      stage('build-docker') {
         steps {
            
             bat "docker-compose up -d" /*don't work its said docker can't start */ 
            bat "py e2e.py" /*don't work it's said selenium don't exist*/
         }
      }
     
   }
}

pipeline {
   agent any

   stages {
      stage('checkout')
      {
         steps{
         git "https://github.com/CHALASS770/WOG.git"
            }
      }
      
      stage('build-docker') {
         steps {
            
             sh "docker-compose up -d" /*don't work its said docker can't start */ 
            sh "python2.7 e2e.py" /*don't work it's said selenium don't exist*/
         }
      }
     
   }
}

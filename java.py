
     { 
         File file = new File("C:\\Users\\Mayank\\Desktop\\1.txt"); 
         FileInputStream fileStream = new FileInputStream(file); 
         InputStreamReader input = new InputStreamReader(fileStream); 
         BufferedReader reader = new BufferedReader(input); 
           String line; 
           int countWord = 0; 
           int sentenceCount = 0; 
           int characterCount = 0; 
           int paragraphCount = 1; 
           int whitespaceCount = 0;
         while((line = reader.readLine()) != null) 
          { 
              if(line.equals("")) 
             { 
                 paragraphCount++; 
              } 

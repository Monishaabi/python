 void (vector<int>list1, int N) 
 { 
      vector<int> final_list; 
      int n = list1.size(); 
      for (int i = 0; i < N; i++)  
    { 
         int min1 = 9999999; 
         for (int j = 0; j < n; j++) 
        { 
            if (list1[j] < min1) 
                min1 = list1[j]; 
        } 
           list1.erase(remove(list1.begin(),  
                list1.end(), min1),  
                list1.end()); 
          final_list.push_back(min1); 
    } 
        for(int i = 0; i < final_list.size(); i++) 
        cout << final_list[i] << " "; 
  }  

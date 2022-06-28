public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        Array.Sort(arr);
        
         int[] array = new int[arr.Length];
        int count=1;
        int b=0;
        
        for(int i=0;i<arr.Length-1;i++){
            if(arr[i]==arr[i+1]) 
            {
                count++;
                
            }
            else {
            if(count>0){ array[b]=count; count=1;b++;};
            
            }if(i==arr.Length-2){ array[b]=count; }
        }
        
        Array.Sort(array);
        for(int i=0;i<array.Length-1;i++){
            Console.WriteLine(array[i]);
           if(array[i]>0) if(array[i]==array[i+1]) return false;
            
        }
        
        return true;
    }
}
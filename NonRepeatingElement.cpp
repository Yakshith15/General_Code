#include<bits/stdc++.h>
using namespace std;

int NonRepeatingInteger(int A[],int n){
  for(int i=0;i<n;i++){
      int j;
    for( j=0;j<n;j++){
      if(i!=j && A[i]==A[j]){
        break;
      }
      
    }
    if(j==n){
        return A[i];
      }
  }
  return -1;
}

int main(){
  int n;
  cout<<"ENter the size of the array"<<endl;
  cin>>n;
  int A[n];
  cout<<"ENter the elements of the array"<<endl;
  for(int i=0;i<n;i++){
    cin>>A[i];
  }
  cout<<NonRepeatingInteger(A,n)<<endl;
  
  return 0;
}

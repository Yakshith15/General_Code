#include<bits/stdc++.h>
using namespace std;

int hcf(int a,int b){
  if(b==0)
    return a; 
  return hcf(b,a%b);  
}
int LCM(int a,int b){
    return a*b/(hcf(a,b));
}

int main(){
  int a,b;
  cout<<"Enter the Numbers"<<endl;
  cin>>a>>b;
  cout<<LCM(a,b)<<endl;
  return 0;
}

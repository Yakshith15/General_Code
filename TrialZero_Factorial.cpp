#include<bits/stdc++.h>
using namespace std;

int TrialZeros(int a){
    int count=0;
    for(int i=5;i<=a;i=i*5){
        count+=a/i;
    }
    return count;
}

int main(){
  int a;
  cout<<"Enter the Number"<<endl;
  cin>>a;
  cout<<TrialZeros(a)<<endl;
  return 0;
}

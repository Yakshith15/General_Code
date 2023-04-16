//So the problem gives two arrays which gives the arriving and leaving time of a single person and the size of array determines the total number of persons to print the maximun number of person at a time in the hotel
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout<<"Enter the size of the array"<<endl;
    cin>>n;
    cout<<"Enter the entry time of the ppl\n";
    vector<int> v(1000,0);//the entry and departures are less than 1000
    int t=0;
    for(int i=0;i<n;i++){
        cin>>t;
        v[t]++;
    }
    cout<<"enter the departures of them\n";
    for(int i=0;i<n;i++){
        cin>>t;
        v[t]--;
    }
    int ans=v[1];
    for(int i=2;i<=1000;i++){
        v[i]=v[i]+v[i-1];

        if(v[i]>ans){
            ans=v[i];
        }
    }
    cout<<ans<<endl;


    return 0;
}

#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int t;
    while(cin>>t){
        for(int i;i<t;i++){
            int x,m,n;
            cin>>x>>m>>n;
            long long sum=0;
            for(int j=m;j<=n;j++){
                sum+=pow(x,j);
            }
            cout<<sum<<'\n';
        }
    }
    return 0;
}
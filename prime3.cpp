#include<iostream>
using namespace std;
 
int main(){
    int n=9;
    bool isprime = true;

    for(int i=2 ;i*i <=n ; i++){
        if(n%i==0){
            isprime= false;
            break;
          
        }
    }
    if(isprime==true){
        cout<<"it is a prime number";
    }else {
        cout<<"it is not a prime number";
    }

    return 0;
}
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
* Clase Linea
*/

namespace myvec{
class Vector{


    public:
    
        int n;
        vector<int> a{vector<int>(5,0)};        
            
        Vector(int _n){
            vector<int> a{vector<int>(5,0)};     
            n = _n;     
        };
       

        
        void size(void){
            cout<< a.size() << endl;
        };
        
        void PrintVec(void){
            cout << "(" << " ";
            for(int i=0;i<5;i++){
                cout << a[i] << " ";
            }
        
            cout << ")" << endl;
        }
        
        void SetPos(int ent, int val){
            a[ent] = val;
        }
        
        int GetPos(int ent){
            return a[ent];
        }
        
        int GetSize(void){
            return a.size();
        }
        
        Vector operator+(const Vector& ve) {

         	    Vector sum(4);
         	    sum.a[0]=this->a[0] + ve.a[0];
         	    sum.a[1]=this->a[1] + ve.a[1];
         	    sum.a[2]=this->a[2] + ve.a[2];
         	    sum.a[3]=this->a[3] + ve.a[3];
         	    sum.a[4]=this->a[4] + ve.a[4];   

         	    return sum;
        }
        
        Vector operator-(const Vector& ve) {

         	    Vector dif(4);
         	    dif.a[0]=this->a[0] - ve.a[0];
         	    dif.a[1]=this->a[1] - ve.a[1];
         	    dif.a[2]=this->a[2] - ve.a[2];
         	    dif.a[3]=this->a[3] - ve.a[3];
         	    dif.a[4]=this->a[4] - ve.a[4];   

         	    return dif;
        }
        
        void operator = (const Vector &ve ) {
				a[0]=ve.a[0];
				a[1]=ve.a[1];
				a[2]=ve.a[2];
				a[3]=ve.a[3];
				a[4]=ve.a[4]; 
		}
		
		int &operator[](int i) {
			
         			return a[i];
      			}
};
}


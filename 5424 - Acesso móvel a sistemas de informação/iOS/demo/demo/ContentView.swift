//
//  ContentView.swift
//  demo
//
//  Created by Gonçalo Feliciano on 08/07/2024.
//

/*
 
 z-index:
 
 */

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack{
            

            Text("GF")
                .frame(width: 200, height: 200)
                .background(Color(red: 156.normalizar(),
                                  green: 156.normalizar(),
                                  blue: 0.normalizar()))
            
                .font(.system(size: 90))
                .foregroundColor(Color(red: 250.normalizar(), green: 250.normalizar(), blue: 0))
                .clipShape(/*@START_MENU_TOKEN@*/Circle()/*@END_MENU_TOKEN@*/)
            
            Text("txt 1")
                .background(.blue)
                .foregroundColor(.white)
                .font(.title2)
                .fontWeight(.bold)
                .clipShape(Capsule())
                .frame(width: 150, height: 60, alignment: .center)
                .background(.gray)
                .clipShape(Circle())

            
            HStack{
                Spacer()
                Text("txt 2")
                Spacer()
                Text("txt 3")
                Spacer()
            }
            
            Button{
                print(156.normalizar())
                
            } label: {
                Text("txt 1")
                    .frame(width: 150, height: 60, alignment: .center)
                    .background(.blue)
                    .foregroundColor(.white)
                    .font(.title2)
                    .fontWeight(.bold)
                    .clipShape(Capsule())
            }
          
        }
    }
}

#Preview {
    ContentView()
}

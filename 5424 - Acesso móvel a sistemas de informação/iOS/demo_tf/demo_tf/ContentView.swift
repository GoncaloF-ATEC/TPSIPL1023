//
//  ContentView.swift
//  demo_tf
//
//  Created by Gonçalo Feliciano on 10/07/2024.
//

import SwiftUI

struct ContentView: View {
    @State var txt = "Hello, worl"

    @State var txtTF = ""
    @State var sliderVal = 5.0

    @State private var current = 170.0
       @State private var minValue = 50.0
       @State private var maxValue = 170.0
       let gradient = Gradient(colors: [.green, .yellow, .orange, .red])

           
           
           
    var body: some View {
        VStack {
            
            
            
            Text(txt)
        
            
           TextField("Nome: ", text: $txtTF)
                .frame(width: 200)
                .textFieldStyle(.roundedBorder)
                .foregroundColor(.gray)
                
              
            Gauge(value: 0.3, in: /*@START_MENU_TOKEN@*/0...1/*@END_MENU_TOKEN@*/) {
                /*@START_MENU_TOKEN@*/Text("Label")/*@END_MENU_TOKEN@*/
            }
            .gaugeStyle(.accessoryCircular)
            
            
            Button(action: {
                txt = txtTF
                
            }, label: {
                Text("Button")
            })
            
            
            Slider(value: $sliderVal, in: 0...10, step: 1.0)
            Text("\(sliderVal)")
            
            
            Gauge(value: current, in: minValue...maxValue) {
                        Image(systemName: "heart.fill")
                            .foregroundColor(.red)
                    } currentValueLabel: {
                        Text("\(Int(current))")
                            .foregroundColor(Color.green)
                    } minimumValueLabel: {
                        Text("\(Int(minValue))")
                            .foregroundColor(Color.green)
                    } maximumValueLabel: {
                        Text("\(Int(maxValue))")
                            .foregroundColor(Color.red)
                    }
                    .gaugeStyle(.accessoryCircular)
                }
        .padding()
    }
}

#Preview {
    ContentView()
}

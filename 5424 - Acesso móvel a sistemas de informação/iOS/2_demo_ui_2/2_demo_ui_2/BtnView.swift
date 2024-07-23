//
//  BtnView.swift
//  2_demo_ui_2
//
//  Created by Gonçalo Feliciano on 16/07/2024.
//

import SwiftUI

struct BtnView: View {
    
    var txt: String
    var body: some View {
        Text(txt)
            .frame(width: 200, height: 60, alignment: .leading)
            .padding([.leading],  CGFloat(15.0))
            .background(.blue)
            .foregroundStyle(.white)
            .font(.title)
            .bold()
            .clipShape(Capsule())
    }
}

#Preview {
    BtnView(txt: "Btn")
}

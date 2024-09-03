//
//  ListLineView.swift
//  Listas
//
//  Created by Gonçalo Feliciano on 23/07/2024.
//

import SwiftUI

struct ListLineView: View {
    
    var nome:String
    
    var body: some View {
        Text(nome)
            .font(.title3)
            .bold()
    }
}

#Preview {
    ListLineView(nome: "Nome")
}

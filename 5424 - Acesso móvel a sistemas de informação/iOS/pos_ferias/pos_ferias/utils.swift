//
//  utils.swift
//  pos_ferias
//
//  Created by Gonçalo Feliciano on 03/09/2024.
//

import Foundation


enum myError:Error{
    case ErroResposta
}


typealias TODOs = [TODO]


/*
 
 {
   "userId": 1,
   "id": 1,
   "title": "delectus aut autem",
   "completed": false
 }
 
 */
struct TODO:Identifiable, Codable{
    
    var userId: Int
    var id: Int
    var title: String
    var completed: Bool
}



class APIHandler: ObservableObject{
    
    var url: URL
    
    @Published var myTodoList:TODOs = []
    
    init(url: String) {
        self.url = URL(string: url)!
    }
    
    
    func getTodo(id: Int) -> TODO?{
        
        if id < 0 || id >= self.myTodoList.count{
            return nil
        }
            
        return myTodoList[id]
    
    }
    
    
    func loadAllData() async throws{
        
        let urlReuquest = URLRequest(url: self.url)
           
        let (data, resp) = try await URLSession.shared.data(for: urlReuquest)
           
        guard let resp = resp as? HTTPURLResponse, (200...299).contains(resp.statusCode) else {
            throw myError.ErroResposta
        }
           
        let myTodoList = try JSONDecoder().decode(TODOs.self, from: data)
           
        self.myTodoList.append(contentsOf: myTodoList)
        
    }
}

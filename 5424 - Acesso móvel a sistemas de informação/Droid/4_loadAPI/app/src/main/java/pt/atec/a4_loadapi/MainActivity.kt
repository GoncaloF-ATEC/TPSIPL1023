package pt.atec.a4_loadapi

import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier

import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory



class MainActivity : ComponentActivity() {

    var api = Retrofit.Builder()
        .baseUrl("https://jsonplaceholder.typicode.com")
        .addConverterFactory(GsonConverterFactory.create())
        .build()
        .create(APIHandler::class.java)



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {

            Column(
                Modifier.fillMaxSize(),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ){

                Button(onClick = {
                    loadAllComments()

                }) {
                    Text("Load all comments")

                }



                Button(onClick = {
                    loadOneComment(12)
                }) {
                    Text("Load one comment")

                }

            }

        }
    }

    fun loadAllComments(){

            this.api.getCommnets().enqueue(object: Callback<List<Comment>> {

                override fun onResponse(
                    call: Call<List<Comment>>,
                    response: Response<List<Comment>>
                ) {

                    if (response.isSuccessful){

                        /*
                        response.body()?.let {
                            for (cmt in it){
                                Log.i("Aula", cmt.name)
                            }
                        }
                        */


                        for (cmt in response.body()!!){
                            Log.i("Aula", cmt.name)
                        }


                        Log.i("Aula", "Tudo Correu bem ${response.code()}")
                    }else{
                        Log.i("Aula", "Algo correu mal ${response.code()}")
                    }
                }


                override fun onFailure(call: Call<List<Comment>>, t: Throwable) {
                    Log.i("Aula", "Erro: ${t.message}")
                }
            }
        )
        Log.i("Aula", "loadAllComments")

    }

    fun loadOneComment(id: Int){

        this.api.getCommnet(id).enqueue(object: Callback<Comment>{

            override fun onResponse(call: Call<Comment>, response: Response<Comment>) {
               if (response.isSuccessful){

                  Log.i("Aula1", "${response.body()?.name}")

               }




            }


            override fun onFailure(call: Call<Comment>, t: Throwable) {
                Log.i("Aula", "Erro: ${t.message}")
            }

            }
        )





        Log.i("Aula", "load Comment -  $id")

    }


}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}



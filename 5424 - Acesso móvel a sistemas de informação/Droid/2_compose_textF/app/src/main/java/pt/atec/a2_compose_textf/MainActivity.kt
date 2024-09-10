package pt.atec.a2_compose_textf

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.material3.TextFieldColors
import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.blur
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import pt.atec.a2_compose_textf.ui.theme._2_compose_textFTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            var nome by remember {
                mutableStateOf("Sem nome")
            }
            var nome_tf = remember {
                mutableStateOf("")
            }

            Column {
                Spacer(modifier = Modifier.height(25.dp))

                Text(nome, modifier = Modifier.padding(10.dp))


                myTextField(nome_tf)

                Button(onClick = {
                    if (nome_tf.value.length > 4 ){
                        nome = nome_tf.value
                        nome_tf.value = ""
                    }

                }) {
                    Text("ok")
                }
            }

        }
    }
}



@Composable
fun myTextField(nome_tf: MutableState<String>){

    TextField(value = nome_tf.value,
        onValueChange = {
            nome_tf.value = it
        },
        label = { Text("Nome: ") },

    )
}

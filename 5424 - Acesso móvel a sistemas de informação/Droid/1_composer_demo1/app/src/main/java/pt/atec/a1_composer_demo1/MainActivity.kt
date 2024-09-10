package pt.atec.a1_composer_demo1

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Button
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Shape
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import pt.atec.a1_composer_demo1.ui.theme._1_composer_demo1Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            //@State var txt = "Ola Mundo"
            var txt by remember {
                mutableStateOf("Ola Mundo")
            }

            var txt2 = remember {
                mutableStateOf("Ola Mundo 2")
            }


            Column {
                Spacer(modifier = Modifier.height(20.dp) )

                Text(txt,
                    fontSize = 19.sp,
                    fontWeight = FontWeight.Bold,
                    fontStyle = FontStyle.Italic,
                    fontFamily = FontFamily.Serif,
                    color = Color.Magenta,
                    letterSpacing = 0.sp,
                    modifier = Modifier
                        .background(Color.Blue)
                        .padding(10.dp)
                )

                Row(modifier = Modifier.padding(top = 15.dp)) {
                    Button(onClick = {
                       txt = "Gonçalo"
                    }) { Text("Btn 1") }

                    Spacer(modifier = Modifier.width(60.dp) )
                }

                Spacer(modifier = Modifier.height(40.dp))


                Text(txt2.value,
                    fontSize = 19.sp,
                    fontWeight = FontWeight.Bold,
                    fontStyle = FontStyle.Italic,
                    fontFamily = FontFamily.Serif,
                    color = Color.Magenta,
                    letterSpacing = 0.sp,
                    modifier = Modifier
                        .background(Color.Blue)
                        .padding(10.dp)
                )

                Row(modifier = Modifier.padding(top = 15.dp)) {
                    Button(onClick = {
                        txt2.value = "Gonçalo 2"
                    }) { Text("Btn 2") }

                    Spacer(modifier = Modifier.width(60.dp) )
                }



            } // column 1



        }
    }
}




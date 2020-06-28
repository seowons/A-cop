
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.res.AssetFileDescriptor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.Matrix;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.widget.ImageView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.bumptech.glide.RequestBuilder;
import com.bumptech.glide.request.RequestOptions;
import com.bumptech.glide.request.target.CustomTarget;
import com.bumptech.glide.request.target.SimpleTarget;
import com.bumptech.glide.request.transition.Transition;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

import org.tensorflow.lite.Interpreter;

import java.io.FileInputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.Arrays;

import javax.xml.transform.Result;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();
    private int REQUEST_IMAGE_CAPTURE = 100;

    // 사진 촬영 버튼 클릭 이벤트
    @OnClick(R.id.photo_btn)
    void onPhotoClicked() {
        sendTakePhotoIntent();
    }

    // 검색 버튼 클릭 이벤트
    @OnClick(R.id.search_btn)
    void onSearchClicked() {
        // 검색,리스트 액티비티 실행
        Intent intent = new Intent(MainActivity.this, ListActivity.class);
        startActivity(intent);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 뷰 바인딩 라이브러리 (Butterknife)
        ButterKnife.bind(this);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        // 사진 촬영 완료시에 호출됨
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            // 사진 데이터를 받아와서 Bitmap 형식으로 변환환
            Bitmap bitmap = (Bitmap) extras.get("data");

            searchImage(bitmap);
        }
    }



    private void searchImage(Bitmap bitmap) {
        // 비트맵 이미지 28x28로 해상도 변경
        Bitmap resizedBmp = Bitmap.createScaledBitmap(bitmap, 28, 28, true);

        // keras에 넘겨줄 이미지 데이터 배열
        float[][][][] imgArr = new float[1][28][28][3];
        float[][][] img = new float[28][28][3];

        // 결과가 저장될 배열
        float[][] resultArray = {{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};

        // 비트맵 이미지 rgb 값을 소수점으로 변경
        for (int i = 0; i < resizedBmp.getWidth(); i++) {
            float[][] arr = new float[28][3];
            for (int j = 0; j < resizedBmp.getHeight(); j++) {
                int color = resizedBmp.getPixel(i, j);

                float[] temp = {0, 0, 0};
                temp[2] = Color.red(color) / 256f;
                temp[1] = Color.green(color) / 256f;
                temp[0] = Color.blue(color) / 256f;

                arr[j] = temp;
            }

            img[i] = arr;
        }

        imgArr[0] = img;

        try {
            // tflite 파일 로딩
            AssetFileDescriptor fileDescriptor = getAssets().openFd("model1.tflite");

            FileInputStream inputStream = new FileInputStream(fileDescriptor.getFileDescriptor());
            FileChannel fileChannel = inputStream.getChannel();
            long startOffset = fileDescriptor.getStartOffset();
            long declaredLength = fileDescriptor.getDeclaredLength();

            ByteBuffer tfLiteFile = fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength);

            // 텐서플로우로 이미지 데이터 전달, resultArray에 결과값 저장됨
            Interpreter interpreter = new Interpreter(tfLiteFile);
            interpreter.run(imgArr, resultArray);

            float result = 1;
            int index = 0;

            // 결과값 중 1에 가장 가까운 값을 검색
            for (float[] output : resultArray) {
                for (int i = 0; i < output.length; i++) {
                    if (Math.abs(1 - output[i]) < result) {
                        result = Math.abs(1 - output[i]);
                        index = i;
                    }
                }
            }

            // 결과값을 결과 액티비티로 전달
            Intent intent = new Intent(MainActivity.this, ResultActivity.class);
            intent.putExtra("result", index);
            startActivity(intent);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendTakePhotoIntent() {
        // 사진 촬영 호출
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
    }
}

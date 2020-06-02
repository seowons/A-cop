package com.github.dudgns0507.keras;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.ListView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.resource.drawable.DrawableTransitionOptions;
import com.google.android.gms.auth.api.signin.internal.Storage;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.ListResult;
import com.google.firebase.storage.StorageReference;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

import butterknife.BindView;
import butterknife.ButterKnife;

public class ResultActivity extends AppCompatActivity {
    private static final String TAG = ResultActivity.class.getSimpleName();

    // 결과 이미지 id 값 리스트
    private ArrayList<Integer> idList = new ArrayList<>(
            Arrays.asList(R.drawable.dumpling, R.drawable.hotdog, R.drawable.fishcake, R.drawable.laver,
                    R.drawable.pancake, R.drawable.pasta, R.drawable.spam, R.drawable.tuna,
                    R.drawable.udon, R.drawable.rice, R.drawable.ramen, R.drawable.chickensoup,
                    R.drawable.soup, R.drawable.tofusushi, R.drawable.tofu, R.drawable.breast,
                    R.drawable.curry, R.drawable.duck, R.drawable.jaban, R.drawable.peachcan));

    @BindView(R.id.result_img)
    ImageView resultImg;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);

        ButterKnife.bind(this);

        Intent intent = getIntent();

        // 전달받은 결과 데이터에 맞는 결과 이미지 로딩
        Glide.with(this)
                .load(idList.get(intent.getIntExtra("result", 0)))
                .into(resultImg);
    }
}

//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_result);
//
//        FirebaseStorage storage = FirebaseStorage.getInstance();
//
//        includesForeCreateReference();
//    }


//    private void listAllFiles() {
//        FirebaseStorage storage = FirebaseStorage.getInstance();
//        StorageReference listRef = storage.getReference().child("files/uid");
//
//        listRef.listAll()
//                .addOnSuccessListener(new OnSuccessListener<ListResult>() {
//                    @Override
//                    public void onSuccess(ListResult listResult) {
//                        for(StorageReference prefix : listResult.getPrefixes()) {
//
//                        }
//
//                        for(StorageReference item : listResult.getItems()) {
//
//                        }
//                    }
//                })
//                .addOnFailureListener(new OnFailureListener() {
//                    @Override
//                    public void onFailure(@NonNull Exception e) {
//
//                    }
//                });
//    }
//
//    private void listAllPaginated(@Nullable String pageToken) {
//        FirebaseStorage storage = FirebaseStorage.getInstance();
//        StorageReference listRef = storage.getReference().child("files/uid");
//
//        Task<ListResult> listPageTask = pageToken != null
//                ? listRef.list(100, pageToken)
//                : listRef.list(100);
//        listPageTask
//                .addOnSuccessListener(new OnSuccessListener<ListResult>() {
//                    @Override
//                    public void onSuccess(ListResult listResult) {
//
//                    }
//                });
//    }
//
//}
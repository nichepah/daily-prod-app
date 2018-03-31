package com.example.pa.sailproduction;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;

public class XroadSSP extends AppCompatActivity implements DatePicker.OnDateChangedListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xroad_ssp);

        DatePicker datePicker = findViewById(R.id.datePicker_ssp);
        //int day = datePicker.getDayOfMonth();
        datePicker.init(datePicker.getYear(), datePicker.getMonth(), datePicker.getDayOfMonth(), this);

    }

    /** Called when user taps GetLatest Button */
    public void getSSPData(View view) {
        Intent intent = new Intent(this, DisplayDataSSP.class);
        startActivity(intent);
    }

    @Override
    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
        String myDate = String.valueOf(year)+"-"+String.valueOf(++monthOfYear)+"-"+String.valueOf(dayOfMonth);
        Intent intent = new Intent(this, DateDisplaySSP.class);
        intent.putExtra("ProdDate", myDate);
        startActivity(intent);
    }
}

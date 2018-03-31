package com.example.pa.sailproduction;

import android.app.DatePickerDialog;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.Toast;

public class XroadG5 extends AppCompatActivity implements DatePicker.OnDateChangedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xroad_g5);

        DatePicker datePicker = findViewById(R.id.datePicker_g5);
        //int day = datePicker.getDayOfMonth();
        datePicker.init(datePicker.getYear(), datePicker.getMonth(), datePicker.getDayOfMonth(), this);

        //datePicker.setOnClickListener();
    }

    /** Called when user taps GetLatest Button */
    public void getG5Data(View view) {
        Intent intent = new Intent(this, DisplayDataG5.class);
        startActivity(intent);
    }

    @Override
    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
        //Toast.makeText(getApplicationContext(), String.valueOf(year), Toast.LENGTH_LONG).show();

        String myDate = String.valueOf(year)+"-"+String.valueOf(++monthOfYear)+"-"+String.valueOf(dayOfMonth);
        Intent intent = new Intent(this, DateDisplayG5.class);
        intent.putExtra("ProdDate", myDate);
        startActivity(intent);

    }
}

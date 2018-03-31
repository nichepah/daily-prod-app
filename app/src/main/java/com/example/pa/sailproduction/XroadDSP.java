package com.example.pa.sailproduction;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;

public class XroadDSP extends AppCompatActivity implements DatePicker.OnDateChangedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xroad_dsp);
    }

    /** Called when user taps GetLatest Button */
    public void getDSPData(View view) {
        Intent intent = new Intent(this, DisplayDataDSP.class);
        startActivity(intent);

        DatePicker datePicker = findViewById(R.id.datePicker_dsp);
        datePicker.init(datePicker.getYear(), datePicker.getMonth(), datePicker.getDayOfMonth(), this);

    }

    @Override
    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {

        String myDate = String.valueOf(year)+"-"+String.valueOf(++monthOfYear)+"-"+String.valueOf(dayOfMonth);
        Intent intent = new Intent(this, DateDisplayDSP.class);
        intent.putExtra("ProdDate", myDate);
        startActivity(intent);
    }
}

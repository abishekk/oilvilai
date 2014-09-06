package com.bignerdranch.android.criminalintent;

import com.bignerdranch.android.criminalintent.Crime;

public interface Callbacks {
    void onCrimeSelected(Crime crime);
    void onCrimeUpdated(Crime crime);
}

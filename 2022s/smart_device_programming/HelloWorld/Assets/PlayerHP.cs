using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class PlayerHP : MonoBehaviour
{
    public TextMeshProUGUI HPText;
    
    void Start()
    {
        HPText.text = "100";
    }
}

// Copyright (c) 2014 Intel Corporation. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.xwalk.embedding.test.v5;

import org.xwalk.embedding.base.XWalkViewTestBase;
import android.annotation.SuppressLint;
import android.test.suitebuilder.annotation.SmallTest;

@SuppressLint("NewApi")
public class XWalkViewTest extends XWalkViewTestBase {

    @SmallTest
    public void testSetUserAgentString() {
        try {
            getInstrumentation().runOnMainSync(new Runnable(){
                @Override
                public void run() {
                    mXWalkView.setUserAgentString(USER_AGENT);
                }
            });
            loadDataSync(null, EMPTY_PAGE, "text/html", false);
            String result = executeJavaScriptAndWaitForResult("navigator.userAgent;");
            assertEquals(EXPECTED_USER_AGENT, result);
        } catch (Exception e) {
            e.printStackTrace();
            assertTrue(false);
        }
    }
}
